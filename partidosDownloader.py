from robobrowser import RoboBrowser
from requests import Session

session = Session()
session.verify = False  # Skip SSL verification

browser = RoboBrowser(session=session,parser="lxml", user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0 (Pale Moon)")
browser.open("https://servicio.mir.es/nfrontal/webpartido_politico.html")

signup_form = browser.get_form(action='webpartido_politico/partido_politicoBuscar.html')
browser.submit_form(signup_form)

resultado = browser.parsed.find(id="resultado")

with open("partidos.txt", "w+") as file:
    for fila in resultado.findAll("tr"):
        for campo in fila.findAll("td"):
            campo = campo.text.replace('\n', '').replace('\t', '').replace('       ', ' ').strip()
            file.write(campo + '\t')
        file.write('\n')

    for x in range(2, 189):
        print(x)
        browser.open("https://servicio.mir.es/nfrontal/webpartido_politico/partido_politicoBuscar.html?pagActual=" + str(x))
        resultado = browser.parsed.find(id="resultado")
        for fila in resultado.findAll("tr"):
            for campo in fila.findAll("td"):
                campo = campo.text.replace('\n', '').replace('\t', '').replace('       ', ' ').strip()
                file.write(campo + '\t')
            file.write('\n')
