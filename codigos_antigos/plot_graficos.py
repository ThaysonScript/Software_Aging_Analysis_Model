#!/usr/bin/env python3

try:
    import matplotlib.pyplot as plt
    import pandas as pd
    import scipy.stats as stats
    from sklearn.linear_model import LinearRegression
    
except ImportError as e:
    print(f'Erro de importação: {e}')
    exit(1)

plt.close('all')

MONITORING_FILES_PATH = './data_logs/logs/'
monitoring_cpu = MONITORING_FILES_PATH + 'machine_monitoring-cpu.csv'
monitoring_disks = MONITORING_FILES_PATH + 'machine_monitoring-disk.csv'
monitoring_zumbies = MONITORING_FILES_PATH + 'machine_monitoring-zombies.csv'
monitoring_mem = MONITORING_FILES_PATH + 'machine_monitoring-mem.csv'
monitoring_VboxHeadless = MONITORING_FILES_PATH + 'monitoring-VBoxHeadless.csv'
monitoring_VboxSvc = MONITORING_FILES_PATH + 'monitoring-VBoxSVC.csv'
monitoring_VboxXPCOMIPCD = MONITORING_FILES_PATH + 'monitoring-VBoxXPCOMIPCD.csv'
server_response_time_monitoring = MONITORING_FILES_PATH + 'response_times.csv'

def plot(filename, ylabel, datetime="date_time", title=None, separator=';', decimal_separator=",", dayfirst=False, division=1, includeColYlabel=False, cols_to_divide=[]):
    df = pd.read_csv(filename, sep=separator, decimal=decimal_separator, dayfirst=dayfirst, parse_dates=[datetime]).rename(columns={datetime: 'seconds'})

    df['seconds'] = (df['seconds'] - df['seconds'][0]).dt.total_seconds() / 3600
    df = df.set_index('seconds').replace(',', '.', regex=True).apply(lambda x: pd.to_numeric(x, errors='ignore'))

    cols_to_divide = cols_to_divide if len(cols_to_divide) != 0 else df.columns
    df[cols_to_divide] = df[cols_to_divide].div(division)


    for col in df.columns:
        col_mix = col + " " + ylabel if type(ylabel) is str and includeColYlabel else ylabel

        df[col] = df[col].fillna(0)

        x = df.index.to_numpy().reshape((-1, 1))
        y = df[col].to_numpy().reshape((-1, 1))

        model = LinearRegression()
        model.fit(x, y)

        Y_pred = model.predict(x)

        ax = df.plot(
            y=col,
            legend=0,
            xlabel='Time(h)',
            ylabel=col_mix if type(ylabel) is str else ylabel[col] if type(ylabel) is dict and col in ylabel else col,
            title=title if type(title) is str else title[col] if type(title) is dict and col in title else col,
            figsize=(10,5),
            style='k',
        )

        # Adicionar a linha da regressão
        ax.plot(x, Y_pred, color='red')
        plt.show()
        fig = ax.get_figure()
        fig.savefig(f'./plot_images/{title}-{col}.png')


plot(title="CPU",filename=monitoring_cpu, ylabel='(percentage)', dayfirst=True, includeColYlabel=True)

plot(itle="Disk", filename=monitoring_disks, ylabel='Disk usage (GB)', dayfirst=True, division=1048576)

plot(title="Zumbis", filename=monitoring_zumbies, ylabel='Zumbis processes(qtt)', dayfirst=True)

plot(title="Memory", filename=monitoring_mem, ylabel='(MB)', dayfirst=True, division=1024, includeColYlabel=True)

plot(
    title="Process - VBoxHeadless", filename=monitoring_VboxHeadless, cols_to_divide=["vmrss","vsz","swap"],
    ylabel={
        'cpu': 'CPU usage (percentage)',
        "vmrss": "Physical memory usage(MB)",
        "vsz": "Virtual memory usage (MB)",
        "swap": "Swap used(MB)",
        'mem': 'Memory usage (percentage)',
        "thread": "Number of threads(qtt)"
    },
    division=1024, dayfirst=True
)

plot(
    title="Process - VBoxSVC", filename=monitoring_VboxSvc, cols_to_divide=["vmrss","vsz","swap"],
    ylabel={
        'cpu': 'CPU usage (percentage)',
        "vmrss": "Physical memory usage(MB)",
        "vsz": "Virtual memory usage (MB)",
        "swap": "Swap used(MB)",
        'mem': 'Memory usage (percentage)'
    },
    division=1024, dayfirst=True
)

plot(
    title="Process - VBoxXPCOMIPCD", filename=monitoring_VboxXPCOMIPCD, cols_to_divide=["vmrss", "vsz", "swap"],
    ylabel={
        'cpu': 'CPU usage (percentage)',
        "vmrss": "Physical memory usage(MB)",
        "vsz": "Virtual memory usage (MB)",
        "swap": "Swap used(MB)",
        'mem': 'Memory usage (percentage)'
    },
    division=1024, dayfirst=True
)

plot(title="Server response time", filename=server_response_time_monitoring, ylabel='Response time(s)', division=1000, dayfirst=True)