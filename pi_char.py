import pygal
chart = pygal.Pie()
chart.title="Linguagens"

chart.add('Javaaa',29)
chart.add('Python',25)
chart.add('C++',25)
chart.add('Js',25)

chart.render_to_file('teste.html')

