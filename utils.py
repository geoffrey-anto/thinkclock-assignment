import pandas as pd

def sort_by_time(d):
    return d.sort_values("start_time")

def get_battery_info_by_filename(filename):
    return pd.read_csv(f"./dataset/data/{filename}")["Battery_impedance"]

def parse_complex_number(s):
    s = complex(s)
    return str(f"{s.real},{s.imag}")

def get_rows_by_battery_id(df, battery_id, type="re",freq="0.1"):
    d = df[df['battery_id'] == battery_id]
    d[d["type"] == "impedance"]
    
    if type == "re" or type == "rct":
        if type == "re":
            d = d[d["type"] == "impedance"]
            d = d.drop(columns=['Rct', 'ambient_temperature', 'test_id', 'uid', 'filename', 'Capacity','type', 'battery_id'])
            d = sort_by_time(d)
            return d
        else:    
            d = d[d["type"] == "impedance"]
            d = d.drop(columns=['Re', 'ambient_temperature', 'test_id', 'uid', 'filename', 'Capacity','type', 'battery_id'])
            d = sort_by_time(d)
            return d
    else:
        d = d[d["type"] == "impedance"]
        d = d.drop(columns=['Rct', 'ambient_temperature', 'test_id', 'uid', 'Re', 'Capacity','type', 'battery_id'])
        d = d.join(d["filename"].apply(get_battery_info_by_filename))
        d.drop(columns=["filename"], inplace=True)
        d = sort_by_time(d)
        idx = str(int((float(freq) * 10)))
        d = d.iloc[:, [0, int(idx)]]
        d["Re"] = d[d.columns[1]].apply(lambda x: float(parse_complex_number(x).split(',')[0]))
        d["Im"] = d[d.columns[1]].apply(lambda x: float(parse_complex_number(x).split(',')[1]))
        d.drop(columns=[d.columns[1]], inplace=True)
        return d["Re"].to_list(), d["Im"].to_list()