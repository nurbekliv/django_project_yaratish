from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def first_views(request):
    html=f"""
        <a href='pages/salah'> salah </a> <br>
        <a href='pages/alisson'> alisson becker </a> <br>
        <a href='pages/virgil'> van dijk </a> <br>
        <a href='pages/gomez'> qirol </a>  <br>
        <a href='pages/konate'> konate </a>
        """
    return HttpResponse(html)


def pages(request,page):
    if page== 'salah':
        html = f"""
                <h1>pages:{page} </h1>
                <p>Mohamed Salah Hamed Mahrous Ghaly (Arabic: محمد صلاح حامد محروس غالي, Egyptian Arabic pronunciation: [mæˈħam.mæd sˤɑˈlɑːħ ˈɣæːli];[5] born 15 June 1992), known as Mohamed Salah or Mo Salah, is an Egyptian professional footballer who plays as a right winger or forward for Premier League club Liverpool and captains the Egypt national team. Regarded as one of the best players of his generation and among the greatest African players of all time, he is known for his clinical finishing, dribbling and speed.[6][7][8]</p>
                <a href='../'> orqaga </a>
                """
    elif page=="alisson":
        html = f"""
                <h1>pages:{page} </h1>
                <p>Álisson Ramsés Becker (born 2 October 1992), known as Alisson Becker or simply Alisson, is a Brazilian professional footballer who plays as a goalkeeper for Premier League club Liverpool and the Brazil national team. Regarded as one of the best goalkeepers in the world,[4] he is renowned for his immense shot stopping, distribution and ability in one-on-one situations.</p>         
                """
    elif page=="virgil":
        html = f"""
                <h1>pages:{page} </h1>
                <p>Virgil van Dijk (Dutch pronunciation: [ˈvɪr.d͡ʒɪl vɑn.ˈdɛik];[2] born 8 July 1991) is a Dutch professional footballer who plays as a centre-back for and captains both Premier League club Liverpool and the Netherlands national team. Widely regarded as one of the best defenders of his generation, he is known for his strength, leadership, speed and aerial ability.[3][4][5][6][7]   </p>         
                """
    elif page=="gomez":
        html = f"""
                <h1>pages:{page} </h1>
                <p>Joseph Dave Gomez (born 23 May 1997) is an English professional footballer who plays as a defender for Premier League club Liverpool and the England national team.

Gomez began his career at Charlton Athletic, breaking into the first team at 17 and playing one full season before joining Liverpool in June 2015. After establishing himself as a first-team regular, Gomez struggled with injuries, but appeared in the 2019 UEFA Champions League final as Liverpool won the competition. He played in the final of the 2019 FIFA Club World Cup with Liverpool winning the competition for the first time in the club's history. He was part of the team that won the 2019–20 Premier League, Liverpool's first league title in 30 years</p>         
                """
    elif page=="konate":
        html = f"""
                <h1>pages:{page} </h1>
                <p>Ibrahima Konaté (born 25 May 1999) is a French professional footballer who plays as a centre-back for Premier League club Liverpool and the France national team.

Starting off with Sochaux, Konaté moved to RB Leipzig in 2017. After four years with the club, Liverpool signed him in 2021 for a fee of £36 million. He won the EFL Cup and FA Cup in his first season.</p>         
                """
    else:
        html=f"""
        page:{page}
        """
    return HttpResponse(html)