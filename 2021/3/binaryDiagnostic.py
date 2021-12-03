# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 07:51:39 2021

@author: backm
"""

import pandas as pd
import numpy as np

bd_in = np.loadtxt("input.txt", dtype=str)


cols = [f"pos{n}" for n in range(len(bd_in[0]))]
values = [[ns[n] for ns in bd_in] for n in range(len(bd_in[0]))]
df = pd.DataFrame.from_dict(dict(zip(cols, values)))

gamma_rate_bin = "".join(df.mode().loc[0].to_list())
epsilon_rate_bin = "".join("1" if x == "0" else "0" for x in gamma_rate_bin)

gamma_rate_dec = int(gamma_rate_bin, 2)
epsilon_rate_dec = int(epsilon_rate_bin, 2)


answer1 = gamma_rate_dec*epsilon_rate_dec


def bitCriteria(df, mode=True):
    """


    Parameters
    ----------
    df : pandas DataFrame
        Dataframe with bit encoded data per column
    mode : bool, optional
        result by mode (True) or by antimode (False). The default is True.

    Returns
    -------
    df_out : pandas DataFrame
        Filtered df as son as it contain only one row.

    """
    df_out = df.copy()
    for i in range(len(df.loc[0])):
        mode_filter = "1" if len(df_out[cols[i]].mode(
        ).values) > 1 else df_out[cols[i]].mode().values[0]
        if not mode:
            mode_filter = "0" if mode_filter == "1" else "1"
        df_filtered = df_out[df_out[cols[i]] == mode_filter]
        if len(df_filtered) >= 1:
            df_out = df_filtered
        else:
            break
    return df_out


oxigen_rating = bitCriteria(df, mode=True)
oxigen_rating_bin = "".join(oxigen_rating.iloc[0].to_list())
oxigen_rating_dec = int(oxigen_rating_bin, 2)


co2_rating = bitCriteria(df, mode=False)
co2_rating_bin = "".join(co2_rating.iloc[0].to_list())
co2_rating_dec = int(co2_rating_bin, 2)


answer2 = oxigen_rating_dec*co2_rating_dec
