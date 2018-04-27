'''
Created on 2018年4月26日

@author: bomber
'''


class HtmlOutputer(object):
    
    def __init__(self):
        self._datas = []
    
    def collect_data(self, data):
        if data is None:
            return
        self._datas.append(data)
    
    def output_html(self):
        fout = open('output.html', 'w',encoding='utf-8')
        fout.write("<html>")
        fout.write("<head>")
        fout.write("<meta charset='utf-8'>")
        fout.write("<head>")
        fout.write("<body>")
        fout.write("<table>")
        
        for data in self._datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")
        
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
    
