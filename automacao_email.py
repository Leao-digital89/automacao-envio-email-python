import pyautogui
import time
import pyperclip

# Abrir o Chrome
pyautogui.press("win")
time.sleep(3)
pyautogui.write("chrome")
time.sleep(3)
pyautogui.press("enter")
time.sleep(30)

# Navegação e cliques
pyautogui.click(x=415, y=375)
time.sleep(10)
pyautogui.click(x=1163, y=150)
time.sleep(20)
pyautogui.click(x=75, y=205)
time.sleep(10)
pyautogui.click(x=850, y=308)
time.sleep(10)

# Inserir destinatários
pyautogui.write("00001164973307SP@al.educacao.sp.gov.br; 00001148649013SP@al.educacao.sp.gov.br; 00001156758142SP@al.educacao.sp.gov.br; 00001152124250SP@al.educacao.sp.gov.br; 00001165917919SP@al.educacao.sp.gov.br; 00001164402092sp@al.educacao.sp.gov.br; 00001158021732SP@al.educacao.sp.gov.br; 00001138434681SP@al.educacao.sp.gov.br; 00001131235605SP@al.educacao.sp.gov.br; 00001141913458SP@al.educacao.sp.gov.br; 0000114883395XSP@al.educacao.sp.gov.br; 00001139524008SP@al.educacao.sp.gov.br; 0000115213517XSP@al.educacao.sp.gov.br; 00001143673116SP@al.educacao.sp.gov.br; 00001164810261SP@al.educacao.sp.gov.br; 00001131545412SP@al.educacao.sp.gov.br; 0000113157834XSP@al.educacao.sp.gov.br; 00001146576109SP@al.educacao.sp.gov.br; 00001134255779SP@al.educacao.sp.gov.br; 00001157619770SP@al.educacao.sp.gov.br; 0000116597356XSP@al.educacao.sp.gov.br; 00001158263946SP@al.educacao.sp.gov.br; 00001152122721SP@al.educacao.sp.gov.br; 0000115092701XSP@al.educacao.sp.gov.br; 00001212479968SP@al.educacao.sp.gov.br; 00001124793288sp@al.educacao.sp.gov.br; 00001130156321SP@al.educacao.sp.gov.br; 00001149620547SP@al.educacao.sp.gov.br; 00001139005534SP@al.educacao.sp.gov.br; 00001152330615SP@al.educacao.sp.gov.br; 00001164410611SP@al.educacao.sp.gov.br; 00001234479758SP@al.educacao.sp.gov.br; 00001164449485SP@al.educacao.sp.gov.br; 00001129508122SP@al.educacao.sp.gov.br; 00001234571493SP@al.educacao.sp.gov.br; 00001154336402SP@al.educacao.sp.gov.br; 00001158739412SP@al.educacao.sp.gov.br")
time.sleep(20)

# Assunto
pyautogui.click(x=816, y=353)
time.sleep(10)
pyautogui.write("Lembrete: Plataforma Matific")

# Corpo do e-mail (corrigido com pyperclip)
pyautogui.click(x=834, y=403)
time.sleep(10)

texto = """Prezados alunos,

Lembro a todos da importância de acessar a plataforma Matific e realizar as atividades propostas. Essas tarefas são fundamentais para o desenvolvimento do raciocínio lógico-matemático e para o acompanhamento do conteúdo trabalhado em sala de aula.

Peço que não deixem de cumprir as atividades dentro do prazo estabelecido.

Atenciosamente,
Professor Everton
"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
