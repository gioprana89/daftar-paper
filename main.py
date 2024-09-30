import streamlit as st 

st.set_page_config(layout="wide")

import pandas as pd

import numpy as np

import plotly.graph_objects as go

import plotly.express as px




st.write('''<style>
         a:hover {
         background-color: yellow;
         text-decoration: none;
         }
         </style>''', unsafe_allow_html=True)




col1, col2, col3 = st.columns(3)

st.image("https://statkomat.com/gambar/ugi.png", caption='', width = 350)

st.markdown("<a href = 'https://statkomat.com/download_tulisan.php' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>STATKOMAT</b></font></a> | <a href = 'https://www.youtube.com/@STATKOMAT/videos' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>YOUTUBE</b></font></a>", unsafe_allow_html=True)


pilih_topik = st.radio(
    "Pilih Bidang: ",
    [":rainbow[Accounting, Finance, Econometrics, Business & Management]", ":rainbow[Psychology]", ":rainbow[Mathematics & Statistics]",      ])


if pilih_topik == ":rainbow[Accounting, Finance, Econometrics, Business & Management]":
    st.markdown("<h2 style='text-align: justify; color: #ffcc00;'><center>Accounting, Finance, Econometrics, Business & Management</center></h2>", unsafe_allow_html=True)

    st.write('''[1] <font color = "#0000ff">Jurnal: <font color = "blue" style="background-color: #d0ff14"><a href = "https://ejournal.usm.my/aamjaf/index" target = '_blank' style = 'text-decoration:none'>The Asian Academy of Management Journal of Accounting and Finance (AAMJAF)</a></font><br>Informasi Biaya: <a href = "https://ejournal.usm.my/aamjaf/publishing-charge" target = '_blank' style = 'text-decoration:none'>With effect from 1st April 2023 onwards, an Article Publishing Charge (APC) of MYR500/USD150 will be imposed on authors upon acceptance of a manuscript for publication (for submission starting 1st April 2023). Upon acceptance of a manuscript, an APC of RM500/USD150 will be imposed on the authors. The APC is based on the followings: (1) MYR500 for corresponding author affiliated mainly to an institution in Malaysia, (2) USD150 for corresponding author affiliated mainly to foreign institution outside Malaysia</a><br>Lama Review: <a href = "https://ejournal.usm.my/aamjaf/policy" target = '_blank' style = 'text-decoration:none'>Typically, the review process will take 60–90 days. Should there be any delay, the Journal will promptly alert the reviewers. For any contradicting reports, the Journal will seek further expert opinion. A revised manuscript may be returned to the initial reviewers. Where manuscript revision is required, authors are urged to ensure that the necessary corrections are made before the manuscript can be accepted for production. Authors will be notified of the decision made by the Editor.</a></font><br><font color = "red"><b>Catatan: Informasi Diakses pada 30 September 2024</b></font><br><br>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://www.scimagojr.com/journalsearch.php?q=19400158801&tip=sid&clean=0">
    <img src="https://statkomat.com/paper-image/Accounting, Finance, Econometrics, Business & Management/1/1.png" width="200">
    </a>""",
    unsafe_allow_html=True)



































































if pilih_topik == ":rainbow[Psychology]":
    st.markdown("<h2 style='text-align: justify; color: #ffcc00;'><center>Psychology</center></h2>", unsafe_allow_html=True)




if pilih_topik == ":rainbow[Mathematics & Statistics]":
    st.markdown("<h2 style='text-align: justify; color: #ffcc00;'><center>Mathematics & Statistics</center></h2>", unsafe_allow_html=True)