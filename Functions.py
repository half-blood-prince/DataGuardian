import pandas as pd
import sys 
import openpyxl
def named_rnage_to_df(xlsx_file,range_name,setindex=False):
    wb = openpyxl.load_workbook(xlsx_file,data_only=True,read_only=True)
    full_range = wb.defined_names[range_name]
    if full_range is None:
        raise ValueError(f"Named range '{range_name}' not found in workbook '{xlsx_file}'")
    destination = list(full_range.destinations)
    if len(destination) > 1:
        raise ValueError(f"Named range '{range_name}' in workbook '{xlsx_file}' has more than one destination")
    ws,reg = destination[0]
    if isinstance(ws,str):
        ws = wb[ws]
    region = ws[reg]
    df = pd.DataFrame([cell.value for cell in row] for row in region)
    df.columns
    df=df[1:]
    if setindex:
        df.set_index(df.columns[0],inplace=True)
        return df
    else:
        return df
def load_file(file,req_col,req_col_flag=True):
    if req_col_flag:
        if file.endswith(".csv"):
            df = pd.read_csv(file,usecols=req_col,low_memory=False,dtype="unicode")
        elif file.endswith(".xlsx"):
            df = pd.read_excel(file,usecols=req_col,low_memory=False,dtype="unicode",engine='openpyxl')
        elif file.endswith(".txt") or file.endswith(".gz") or file.endswith(".zip"):
            df = pd.read_csv(file,usecols=req_col,low_memory=False,dtype="unicode",sep="\t")
        elif file.endswith("xls"):
            df = pd.read_excel(file,usecols=req_col,low_memory=False,dtype="unicode",engine="pyxlsb")
        elif file.endswith(".parquet"):
            df = pd.read_parquet(file,columns=req_col,engine='pyarrow')
        else:
            raise ValueError("File format not supported")
    else:
        if file.endswith(".csv"):
            df = pd.read_csv(file,low_memory=False,dtype="unicode")
        elif file.endswith(".xlsx"):
            df = pd.read_excel(file,low_memory=False,dtype="unicode",engine='openpyxl')
        elif file.endswith(".txt") or file.endswith(".gz") or file.endswith(".zip"):
            df = pd.read_csv(file,low_memory=False,dtype="unicode",sep="\t")
        elif file.endswith("xls"):
            df = pd.read_excel(file,low_memory=False,dtype="unicode",engine="pyxlsb")
        elif file.endswith(".parquet"):
            df = pd.read_parquet(file,engine='pyarrow')
        else:
            raise ValueError("File format not supported")
    return df
def save_data_for_analysis(input_size,output_size,region,name):
    print("Input Size: ",input_size)
    print("After filter Size: ",output_size)
    print("Region: ",region)
    print("Name: ",name)
    try:
        workbook = xw.Book("Analysis.xlsx")
        print("Connected to Analysis.xlsx")
    except:
        workbook = xw.Book()
        workbook.save("Analysis.xlsx")
        print("Created Analysis.xlsx")
    try:
        print("Trying to create a sheet info")
        ws = workbook.sheets.add["Info"]
    except:
        print("Sheet already exists")
        ws = workbook.sheets["Info"]
    app = xw.apps.active
    app.display_alerts = False
    pointer = 2
    ws.range("A"+str(pointer)).value = input_size
    ws.range("B"+str(pointer)).value = output_size
    ws.range("C"+str(pointer)).value = region
    ws.range("D"+str(pointer)).value = name
    try:
        workbook.save(analysis.xlsx)
    except:
        workbook.save()
def filter(dic, input_file_path, output_file_path,region,name):
    print("Filtering")
    print(dic)
    print(input_file_path.get())
    df = pd.read_csv(input_file_path)
    input_size = sys.getsizeof(df)
    column_list = []
    regex_list = []
    for i in dic:
        column_list.append(i)
        regex_list.append(dic[i])
    for i in range(len(column_list)):
        df = df[df[column_list[i]].str.contains(regex_list[i], na=False)]
    output_size = sys.getsizeof(df)
    save_data_for_analysis(input_size,output_size,region,name)
    print(df)
    df.to_csv(output_file_path, index=False)