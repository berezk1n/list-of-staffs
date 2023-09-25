import webbrowser

file_path = 'index.html'

html_string = """
<!DOCTYPE html>
<html>
 <head>
  <title>Импульс</title>
 </head>
 <body>
    <p class = "a"><h2>Список сотрудников компании "Импульс"</h2></p>
    <form method="post" action="program">
    <p class = "b"><i>Отдел разработки:</i> </p>
     <ul>
        <li>Главный разработчик — Фёдоров Руслан</li>
        <li>Младший разработчик — Иванова Ирина</li>
        <li>Тестировщик — Романов Пётр</li>
      </ul>
    <p class = "b"><i>Бухгалтерия:</i> </p>
    <ul>
        <li>Старший бухгалтер — Петров Иван</li>
        <li>Бухгалтер — Антонова Ольга</li>
      </ul>
        <style>
    .a {
  font-size: 25pt; 
  background-color:rgb(255, 255, 255); 
  color: rgb(79, 57, 85) 
     }
  
   .b {
  border: 4px double gainsboro;
  padding:25px;
  border-radius: 50px 50px;
  background-color: rgb(255, 255, 255);
  color: rgb(80, 41, 41);
  font-family: Century, Verdana; 
  font-size: 12pt; 
  background-color:rgb(255, 255, 255); 
  color: rgb(79, 57, 85) 
     }
    }
</style>
    </form>
    </body>
</html>
"""

with open(file_path, 'w', encoding='utf-8') as html_file:
    html_file.write(html_string)

webbrowser.open_new_tab(file_path)