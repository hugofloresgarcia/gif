import pandas as pd
from matplotlib import pyplot as plt
import gif

START = pd.Timestamp('2019-04-20')
END = pd.Timestamp('2020-05-01')

data = '1.9,2.0,3.8,2.9,2.7,1.5,1.4,2.0,1.8,2.6,2.1,1.4,2.8,3.2,3.0,3.6,2.4,4.2,3.3,4.3,2.0,4.0,2.0,2.2,2.5,1.8,1.8,1.6,2.6,2.6,2.8,2.1,2.4,1.9,1.4,1.2,3.9,2.9,1.7,1.8,1.7,2.4,2.3,1.5,2.4,2.6,1.6,1.2,1.9,2.5,2.3,2.6,2.0,1.8,2.5,1.9,2.5,2.7,2.5,2.0,1.6,1.4,2.4,2.4,0.7,3.5,3.6,2.9,3.4,1.6,1.8,1.8,1.1,1.9,1.9,1.3,1.6,2.1,1.7,3.1,4.4,3.7,2.8,3.6,4.0,5.6,2.5,1.4,1.6,1.6,2.9,2.0,2.9,2.0,1.9,1.9,1.9,1.2,2.1,1.8,2.5,2.0,2.0,2.1,2.3,2.9,1.4,1.6,1.4,2.2,2.2,2.4,1.6,1.2,1.8,1.8,2.2,1.8,5.3,0.8,2.1,3.3,4.5,1.4,1.3,2.8,0.9,1.7,1.6,1.3,1.8,2.4,3.6,2.6,3.6,5.8,2.4,1.2,1.5,2.1,2.5,3.1,1.8,2.0,1.6,1.8,3.6,2.2,2.1,2.2,1.0,1.7,2.0,2.3,2.0,1.6,1.6,1.2,1.1,1.6,1.7,2.2,1.5,1.9,1.6,2.0,2.3,1.8,3.2,2.7,2.0,2.3,1.3,1.4,1.0,2.1,1.6,1.6,2.7,2.7,2.9,2.7,2.9,2.5,2.2,2.7,2.5,1.7,3.0,2.9,2.4,3.0,3.1,3.0,3.4,2.2,1.7,4.3,2.8,2.8,2.0,4.3,4.2,7.9,9.1,3.6,2.7,4.9,4.1,4.5,3.1,4.1,3.1,3.0,3.7,2.9,3.0,4.1,4.4,4.8,1.9,2.6,2.3,2.2,1.8,3.7,1.7,1.9,3.5,6.3,3.2,2.2,5.0,1.4,2.8,2.2,2.3,3.6,2.4,3.9,1.7,2.2,1.9,2.5,2.6,3.4,4.8,3.2,5.0,5.8,3.3,3.8,2.6,2.8,3.5,3.2,3.6,3.1,6.3,7.5,3.2,3.5,3.4,4.2,2.7,2.9,6.9,4.3,4.3,2.7,2.7,3.1,4.4,5.8,2.8,3.2,4.1,2.0,3.0,5.1,5.4,6.5,3.0,2.7,2.8,3.1,2.6,4.4,5.7,3.6,3.4,4.1,4.2,4.3,5.6,4.9,2.7,2.1,3.5,3.5,3.1,2.7,0.7,3.1,1.9,3.9,2.9,2.9,2.4,2.5,2.5,3.2,2.1,2.3,2.1,2.3,4.7,4.7,4.4,4.5,4.0,3.4,3.0,1.9,3.8,1.4,2.6,1.7,2.8,2.7,2.7,2.2,2.6,4.3,6.7,7.0,4.2,4.9,3.8,4.8,4.8,3.5,3.0,1.8,1.3,2.4,4.1,4.5,4.6,4.5,4.2,3.4,2.8,1.4,3.0,2.4,2.2,1.9,2.1,1.6,2.8,2.8,4.2,3.1,3.7,2.0,2.6,1.7,2.1,1.6,3.5,1.6,1.8,2.1,3.0,5.4,2.9,3.0'

df = pd.DataFrame({
    'date': pd.date_range(start=START, end=END),
    'time': [float(d) for d in data.split(',')]
})


@gif.frame
def plot(date):
    d = df[df['date'] <= date]
    fig, ax = plt.subplots(figsize=(5, 3), dpi=100)
    plt.plot(d['date'], d['time'])
    ax.set_xlim([START, END])
    ax.set_ylim([0, 10])
    ax.set_xticks([date])
    ax.set_yticks([0, 2, 4, 6, 8, 10])
    ax.set_xticklabels([date.strftime("%b '%y")])
    ax.set_yticklabels([0, 2, 4, 6, 8, '\n10\nhours'])

frames = []
for date in df['date']:
    frame = plot(date)
    frames.append(frame)

gif.save(frames, 'gallery/matplotlib/phone/phone.gif', duration=35)
