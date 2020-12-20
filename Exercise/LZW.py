"""

 Created on 19-Dec-20
 @author: Kiril Zelenkovski

LZW compression algorithm in Python 3.7

"""
import plotly.graph_objects as go

# Имплементација на алгоритамот во Python 3.7
def compress(uncompressed, rules):
    """/TAN/HAN/HAN/AN/"""

    # Build the dictionary.
    # dict_size = 256
    dictionary_LZW = rules
    dict_size = len(rules) + 1
    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary_LZW:
            w = wc
        else:
            result.append(dictionary_LZW[w])
            # Add wc to the dictionary.
            dictionary_LZW[wc] = dict_size
            dict_size += 1
            w = c

    # Output the code for w.
    if w:
        result.append(dictionary_LZW[w])
    return result, dictionary_LZW


# # Compress with LZW algorithm
# compressed, LZW = compress("/TAN/HAN/HAN/AN/")
# # Final output table
# print('For input:/TAN/HAN/HAN/AN/ we get the table: ')
# for key, value in LZW.items():
#     print("{:<10} {:<10}".format(value, key))
#
# # Only output array
# print('And the final output: ')
# print(compressed)


# EXAMPLE 1
uncompressed_string = "/TAN/HAN/HAN/AN/"
# Compress with LZW algorithm
compressed, LZW = compress(uncompressed_string,
                           {'/': 1, 'H': 2, 'A': 3, 'N': 4, 'T': 5})

values = list(LZW.values())
keys = list(LZW.keys())


fig = go.Figure(
    data=[go.Table(
        header=dict(values=['Index', 'Entry'],
                    fill_color='paleturquoise',
                    align='center'),
        cells=dict(values=[values, keys],
                   fill_color='lavender',
                   align='center'))],
    layout = go.Layout(
        margin=dict(l=10, r=10, t=17, b=20, pad=1),
        width=500,
        height=400,
        annotations=[
            dict(
                showarrow=False,
                text='Compressed output for' + uncompressed_string + ':',
                xanchor='right',
                x=1,
                yanchor='top',
                y=0.05),
            dict(
                font=dict(
                color="crimson",
                size=12),
                showarrow=False,
                text=f'{compressed}',
                xanchor='right',
                x=1,
                yanchor='top',
                y=0.005)]))
fig.show()

# EXAMPLE 2
import plotly.graph_objects as go

uncompressed_string = "/THIS/IS/HIS/IS/"
# Compress with LZW algorithm
compressed, LZW = compress(uncompressed_string,
                           {'/': 1, 'H': 2, 'I': 3, 'S': 4, 'T': 5})

values = list(LZW.values())
keys = list(LZW.keys())


fig = go.Figure(
    data=[go.Table(
        header=dict(values=['Index', 'Entry'],
                    fill_color='lightskyblue',
                    align='center'),
        cells=dict(values=[values, keys],
                   fill_color='lightcyan',
                   align='center'))],
    layout = go.Layout(
        margin=dict(l=10, r=10, t=17, b=20, pad=1),
        width=500,
        height=400,
        annotations=[
            dict(
                showarrow=False,
                text='Compressed output for ' + uncompressed_string + ": " ,
                xanchor='right',
                x=1,
                yanchor='top',
                y=0.05),
            dict(
                font=dict(
                color="crimson",
                size=12),
                showarrow=False,
                text=f'{compressed}',
                xanchor='right',
                x=1,
                yanchor='top',
                y=0.005)]))
fig.show()




