from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("disable-content-security-policy")
options.add_argument("--headless")
options.add_argument("--disable-proxy-certificate-handler")
options.add_argument('-allow-running-insecure-content') #options burla algumas restrições e faz com que açoes sejam mais simples no codigo
driver = webdriver.Firefox(options=options)
urls = [ 'https://172.16.7.67/general/information.html?kind=item',
        'http://172.16.7.113/',  
        'http://172.16.7.60/', 
        'https://172.16.7.151/general/status.html', 
        'http://172.16.7.61/',
        'http://172.16.7.41/general/status.html', 
        'http://172.16.7.35/login.html'] #lista de urls pegas
for url in urls:
    driver.get(url)
    titulo = driver.title #pega o titulo
    if titulo == 'Remote UI: Login: iR1643i II: iR1643i II':
      titulo = 'canon 1643'
    if url == 'https://172.16.7.67/general/information.html?kind=item':
        if url == 'https://172.16.7.67/general/information.html?kind=item':
         urlAtual = '172.16.7.67'
        pagina_contador = driver.find_element(By.XPATH,('//*[@id="pageContents"]/form/div[10]/dl/dd[1]'))
        total_pagina = pagina_contador.text
        print("total pag: {}, Titulo: {}, IP: {}".format(total_pagina,titulo,urlAtual))

    if url == 'http://172.16.7.113/':
     if url == 'http://172.16.7.113/':
        urlAtual = '172.16.7.113' #se a url atual for essa ele passa pro print
     botao_login = driver.find_element(By.XPATH,'//*[@id="i0012A"]' )
     botao_login.click()
     label_gerente = driver.find_element(By.XPATH, ('//*[@id="i0014"]')) #primeira caixa de texto das canons
     label_gerente.send_keys('1234567')
     label_senha = driver.find_element(By.XPATH, ('//*[@id="i0016"]'))
     label_senha.send_keys('1234567')
     login_canon = driver.find_element(By.XPATH, ('//*[@id="submitButton"]'))
     login_canon.click()
     MenuDeStatus = driver.find_element(By.XPATH, ('//*[@id="navStandard"]/ul/li[1]/a/span'))
     MenuDeStatus.click()
     Pagina_Contador = driver.find_element(By.XPATH, ('//*[@id="navigation"]/ul[10]/li/a'))
     Pagina_Contador.click()
     pagina_total = driver.find_element(By.XPATH , ('//*[@id="contents"]/div[3]/div/div/table/tbody/tr[1]/td'))
     total_pagina= pagina_total.text
     print("total pag: {}, Titulo: {} IP: {}".format(total_pagina,titulo,urlAtual))
    if url == 'https://172.16.7.151/general/status.html':
     if url == 'https://172.16.7.151/general/status.html':
        urlAtual = '172.16.7.151'
     senha_5652 = driver.find_element(By.XPATH, '//*[@id="LogBox"]')
     senha_5652.send_keys('initpass')
     login_5652 = driver.find_element(By.XPATH, '//*[@id="login"]')
     login_5652.click()
     pagina_contador= driver.find_element(By.XPATH, '//*[@id="subMenu"]/div[3]/a')
     pagina_contador.click()
     total_pagina = driver.find_element(By.XPATH, '//*[@id="pageContents"]/form/div[10]/dl/dd[1]')
     print("total pag: {}, Titulo: {}, IP: {}".format(total_pagina.text,titulo, urlAtual))
    if url == 'http://172.16.7.60/':
       if url == 'http://172.16.7.60/':
        urlAtual = '172.16.7.60'
        botao_gerente = driver.find_element(By.ID ,'i0012A')
        botao_gerente.click()
        label_senha = driver.find_element(By.XPATH, '//*[@id="i0014"]')  
        label_senha.send_keys('1234567')
        label_senha = driver.find_element(By.ID, 'i0016')
        label_senha.send_keys('1234567')
        botao_login = driver.find_element(By.CLASS_NAME, 'ButtonEnable')
        botao_login.click()    
        menuDeStatus = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/ul/li[1]/a/span')    
        menuDeStatus.click()    
        pagina_contador = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[2]/div/ul[10]/li/a')
        pagina_contador.click()
        total_pagina = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div/div/table/tbody/tr[1]/td')
        print("total pag: {}, Titulo: {}, IP: {}".format(total_pagina.text,titulo,urlAtual))
    if url == 'http://172.16.7.61/':
     if url == 'http://172.16.7.61/':
       urlAtual = '172.16.7.61'
     botao_senha = driver.find_element(By.XPATH, '//*[@id="i0012A"]')
     botao_senha.click()
     label_gerente = driver.find_element(By.ID, 'i0014')
     label_gerente.send_keys('1234567')
     label_senha = driver.find_element(By.ID, 'i0016')
     label_senha.send_keys('1234567')
     botao_login = driver.find_element(By.CLASS_NAME, 'ButtonEnable')
     botao_login.click()
     menuDeStatus = driver.find_element(By.XPATH, '//*[@id="navStandard"]/ul/li[1]/a/span')
     menuDeStatus.click()
     pagina_contador = driver.find_element(By.XPATH, '//*[@id="navigation"]/ul[10]/li/a')
     pagina_contador.click()
     total_pagina = driver.find_element(By.XPATH, '//*[@id="contents"]/div[3]/div/div/table/tbody/tr[1]/td')
     print("total pag: {}, Titulo: {}, IP: {} ".format(total_pagina.text,titulo, urlAtual))
    if url == 'http://172.16.7.41/general/status.html':
      if url == 'http://172.16.7.41/general/status.html':
        urlAtual = '172.16.7.41'
      caixa_senha = driver.find_element(By.XPATH, '//*[@id="LogBox"]')
      caixa_senha.send_keys('KhD$8RH$') #send keys passa o que estiver escrito entre parenteses para a caixa que estiver selecionado
      login_canon = driver.find_element(By.ID, 'login')
      login_canon.click()
      pagina_contador = driver.find_element(By.XPATH, '//*[@id="subMenu"]/div[3]/a')
      pagina_contador.click()
      total_pagina = driver.find_element(By.XPATH, '//*[@id="pageContents"]/form/div[9]/dl/dd[1]')
      print("total pag: {}, Titulo: {}, IP: {} ".format(total_pagina.text,titulo, urlAtual))
    if url == 'http://172.16.7.35/login.html':
      if url == 'http://172.16.7.35/login.html':
       urlAtual = '172.16.7.35'
      botao_senha = driver.find_element(By.XPATH, '//*[@id="i0012A"]')
      botao_senha.click()
      label_gerente = driver.find_element(By.ID, 'i0014')
      label_gerente.send_keys('1234567')
      label_senha = driver.find_element(By.ID, 'i0016')
      label_senha.send_keys('1234567')
      botao_login = driver.find_element(By.CLASS_NAME, 'ButtonEnable')
      botao_login.click()
      menuDeStatus = driver.find_element(By.XPATH, '//*[@id="navStandard"]/ul/li[1]/a/span')
      menuDeStatus.click()
      pagina_contador = driver.find_element(By.XPATH, '//*[@id="navigation"]/ul[10]/li/a')
      pagina_contador.click()
      total_pagina = driver.find_element(By.XPATH, '//*[@id="contents"]/div[3]/div/div/table/tbody/tr[1]/td')
      print("total pag: {}, Titulo: {}, IP: {} ".format(total_pagina.text,titulo, urlAtual))


  
