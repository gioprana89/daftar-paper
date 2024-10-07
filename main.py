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





st.write('''<br><br><br><center><font color = "#0000ff" size = 7>Daftar Jurnal Scopus (Gratis & Berbayar)</font></center>



             ''', unsafe_allow_html = True)











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




















    st.write('''<br><br><br>[2] <font color = "#0000ff">Jurnal: <font color = "blue" style="background-color: #d0ff14"><a href = "https://journals.ue.poznan.pl/ebr" target = '_blank' style = 'text-decoration:none'>The Economics and Business Review (earlier as the Poznan University of Economics Review) </a></font><br>Informasi Biaya: <a href = "https://journals.ue.poznan.pl/ebr" target = '_blank' style = 'text-decoration:none'>The EBR invites submissions of original and unpublished articles. The journal is published in English only, with a frequency of four issues yearly. Texts are double-blind reviewed. EBR is an open access journal. To submit, process and publish an article in Economics and Business Review authors are not required to pay any charge.</a><br>Lama Review: <a href = "https://journals.ue.poznan.pl/ebr/review" target = '_blank' style = 'text-decoration:none'>The author is required to send back the corrected article in two versions: with trace changes and a clean copy, along with the answers to the reviews in 30 days – otherwise it will be assumed to have been withdrawn;If a paper’s reviews are mixed the Editorial Board either rejects the submission at that stage or sends it to an additional Reviewer. If the latter option is chosen, the Editorial Board, based on three double-blind reviews takes the final decision whether or not to publish the paper. In cases where a manuscript is returned to an author for major revisions it must be resubmitted within 30 days; otherwise it will be assumed to have been withdrawn.</a></font><br><font color = "red"><b>Catatan: Informasi Diakses pada 1 Oktober 2024</b></font><br><br>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://www.scimagojr.com/journalsearch.php?q=21101026934&tip=sid&clean=0">
    <img src="https://statkomat.com/paper-image/Accounting, Finance, Econometrics, Business & Management/2/1.png" width="200">
    </a>""",
    unsafe_allow_html=True)









    st.write('''<br><br><br>[3] <font color = "#0000ff">Jurnal: <font color = "blue" style="background-color: #d0ff14"><a href = "http://www.sjm06.com/" target = '_blank' style = 'text-decoration:none'>Serbian Journal of Management
</a></font><br>Informasi Biaya: <a href = "http://www.sjm06.com/instr_auth.html" target = '_blank' style = 'text-decoration:none'>Publishing manuscripts in SJM is free of charge. There are no article processing or article submission charges.</a><br>Lama Review: <a href = "http://www.sjm06.com/received.html" target = '_blank' style = 'text-decoration:none'>All papers submitted to the Serbian Journal of Management (SJM) for possible publication  are under Editors Evaluation. Only the articles which are prepared according to the instructions to authors and within the SJMs scope will be further proceded to the reviewing process. Editors evaluation is usually up to 3 months long. However, due to increased number of submissions, sometimes it can be even longer. After this period of time, authors will receive Editors response, with the results of initial Editors evaluation. The manuscripts which are prepared in accordance to Instructions to Authors and which are considered to be at the adequate level of quality to be further processed for publication in SJM,  will be passed to official double blind peer review process.</a></font><br><font color = "red"><b>Catatan: Informasi Diakses pada 2 Oktober 2024</b></font><br><br>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://www.scimagojr.com/journalsearch.php?q=21100305371&tip=sid&clean=0">
    <img src="https://statkomat.com/paper-image/Accounting, Finance, Econometrics, Business & Management/3/1.png" width="200">
    </a>""",
    unsafe_allow_html=True)
















    st.write('''<br><br><br>[4] <font color = "#0000ff">Jurnal: <font color = "blue" style="background-color: #d0ff14"><a href = "https://www.journals.vu.lt/ekonomika/" target = '_blank' style = 'text-decoration:none'>Ekonomika Journal
</a></font><br>Informasi Biaya: <a href = "https://www.journals.vu.lt/ekonomika/about" target = '_blank' style = 'text-decoration:none'>The journal does not charge article processing charges or submission charges.</a><br>Lama Review: <a href = "https://www.journals.vu.lt/ekonomika/information/authors" target = '_blank' style = 'text-decoration:none'>Initial decision to review: 3–5 days after submission. Decision after review: 3–4 weeks after submission. Anticipated timeframe for suggested revisions: 2–3 months (with flexibility if needed). Time to publication: Within 3-5 months of acceptance.</a></font><br><font color = "red"><b>Catatan: Informasi Diakses pada 3 Oktober 2024</b></font><br><br>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://www.scimagojr.com/journalsearch.php?q=21100305371&tip=sid&clean=0">
    <img src="https://statkomat.com/paper-image/Accounting, Finance, Econometrics, Business & Management/4/1.png" width="200"><br>
    <img src="https://statkomat.com/paper-image/Accounting, Finance, Econometrics, Business & Management/4/2.png" width="1200"><br>
    <img src="https://statkomat.com/paper-image/Accounting, Finance, Econometrics, Business & Management/4/3.png" width="700"><br>
    </a>""",
    unsafe_allow_html=True)

















































if pilih_topik == ":rainbow[Psychology]":
    st.markdown("<h2 style='text-align: justify; color: #ffcc00;'><center>Psychology</center></h2>", unsafe_allow_html=True)

    st.write('''[1] <font color = "#0000ff">Jurnal: <font color = "blue" style="background-color: #d0ff14"><a href = "https://www.tandfonline.com/journals/oaps20" target = '_blank' style = 'text-decoration:none'>Cogent Psychology</a></font><br>Informasi Biaya: <a href = "https://www.tandfonline.com/action/authorSubmission?show=instructions&journalCode=oaps20" target = '_blank' style = 'text-decoration:none'>The standard article publishing charge (APC) for this journal is $ 2195 / £ 1756 / EUR 2110 / AUD 3060, plus VAT or other local taxes where applicable in your country. There is no submission charge.</a><br>Lama Review: <a href = "https://www.tandfonline.com/journals/oaps20/about-this-journal#aims-and-scope" target = '_blank' style = 'text-decoration:none'>4 days avg. from submission to first decision; 89 days avg. from submission to first post-review decision; 16 days avg. from acceptance to online publication; 18% acceptance rate</a></font><br><font color = "red"><b>Catatan: Informasi Diakses pada 2 September 2024</b></font><br><br>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://www.scimagojr.com/journalsearch.php?q=21100774706&tip=sid&clean=0">
    <img src="https://statkomat.com/paper-image/Psychology/1/1.png" width="200">
    </a>""",
    unsafe_allow_html=True)





    st.write('''<br><br><br>[2] <font color = "#0000ff">Jurnal: <font color = "blue" style="background-color: #d0ff14"><a href = "http://www.dps.org.rs/en/psihologija-journal/" target = '_blank' style = 'text-decoration:none'>Psihologija Journal</a></font><br>Informasi Biaya: <a href = "http://dps.org.rs/images/How_to_publish_in_Psihologija.pdf" target = '_blank' style = 'text-decoration:none'>Publishing in Psihologija is free - Psihologija is financed by public funds and by the Serbian Psychological Association. There are no charges for authors.</a><br>Lama Review: <a href = "https://www.dps.org.rs/wp-content/uploads/2009/03/Instructions_for_authors.pdf" target = '_blank' style = 'text-decoration:none'>If sent for a review, the paper will be examined by two independent reviewers, and this process normally takes up to three months</a></font><br><font color = "red"><b>Catatan: Informasi Diakses pada 3 September 2024</b></font><br><br>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://www.scimagojr.com/journalsearch.php?q=19200156803&tip=sid">
    <img src="https://statkomat.com/paper-image/Psychology/2/1.png" width="200"><br>
        <img src="https://statkomat.com/paper-image/Psychology/2/2.png" width="400">
    </a>""",
    unsafe_allow_html=True)






















if pilih_topik == ":rainbow[Mathematics & Statistics]":
    st.markdown("<h2 style='text-align: justify; color: #ffcc00;'><center>Mathematics & Statistics</center></h2>", unsafe_allow_html=True)













































st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")




st.markdown(
    """<center><img src="https://statkomat.com/gambar/ugi.png" width="500"></center>
    <h2 style='text-align: justify; color: blue;'><center>Prana Ugiana Gio, Founder of <a href = 'https://statcal.com/' target = '_blank' style = 'text-decoration:none'><font color = 'orange'>STATCAL</a></center></h2>""",
    unsafe_allow_html=True)




col1, col2, col3, col4, col5, col6 = st.columns([2, 2, 2, 2, 2, 2])
with col1:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/logo_figshare2.png" width="50"><br><a href = 'https://figshare.com/authors/prana_ugiana_gio/17826386' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>FIGSHARE</b></font></center></a>""",unsafe_allow_html=True)
with col2:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/statkomat.gif" width="50"><br><a href = 'https://statkomat.com/download_tulisan.php' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>STATKOMAT</b></font></center></a>""",unsafe_allow_html=True)
with col3:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/youtube.png" width="50"><br><a href = 'https://www.youtube.com/@STATKOMAT/videos' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>YOUTUBE</b></font></center></a>""",unsafe_allow_html=True)
with col4:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/literature-review.gif" width="50"><br><a href = 'https://literaturereview.streamlit.app/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>LITERATURE REVIEW</b></font></center></a>""",unsafe_allow_html=True)
with col5:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/list-papers.gif" width="50"><br><a href = 'https://daftar-paper.streamlit.app/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>LIST OF JOURNALS</b></font></center></a>""",unsafe_allow_html=True)
with col6:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/my-papers.gif" width="50"><br><a href = 'https://ugi-publikasi.streamlit.app/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>MY PAPERS</b></font></center></a>""",unsafe_allow_html=True)

st.markdown("")
st.markdown("")

col7, col8, col9, col10, col11, col12 = st.columns([2, 2, 2, 2, 2, 2])
with col7:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/pls-sem.gif" width="50"><br><a href = 'https://aplikasi-plssem.streamlit.app//' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>STRUCTURAL EQUATION MODELING (PLS-SEM)</b></font></center></a>""",unsafe_allow_html=True)
with col8:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/statcal.gif" width="50"><br><a href = 'https://statcal.com/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>STATCAL</b></font></center></a>""",unsafe_allow_html=True)
with col9:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/shiny.gif" width="50"><br><a href = 'https://share-your-shiny-app.id/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>SHINY</b></font></center></a>""",unsafe_allow_html=True)
with col10:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/ugi-gio.gif" width="50"><br><a href = 'https://ugi-gio.id/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>UGI</b></font></center></a>""",unsafe_allow_html=True)
with col11:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/indcomp.gif" width="50"><br><a href = 'https://indcomp-stats.id/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>INDCOMP</b></font></center></a>""",unsafe_allow_html=True)
with col12:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/github.png" width="50"><br><a href = 'https://github.com/gioprana89' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>GITHUB</b></font></center></a>""",unsafe_allow_html=True)







st.markdown("")
st.markdown("")

st.markdown("""<a href = 'https://saweria.co/statkomat' target = '_blank' style = 'text-decoration:none'><center><img src="https://statkomat.com/streamlit-ugi/kopi.gif" width="150"></center></a><br><center><b><a href = 'https://saweria.co/statkomat' target = '_blank' style = 'text-decoration:none'><font color = 'orange' size = 7>Buy Me a Cup of Coffee</font></a></b></font></center>""",unsafe_allow_html=True)










