import io

from django.http import FileResponse
from django.views.generic import View
from reportlab.pdfgen import canvas
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML


class IndexView(View):
    def get(self, request, *args, **kwargs):
        buffer = io.BytesIO()
        pdf = canvas.Canvas(buffer)
        pdf.drawString(280, 800, 'TITLE')
        pdf.showPage()
        pdf.save()
        buffer.seek(0)
        """
        download
        return FileResponse(buffer,
                            as_attachment=True,
                            filename='report.pdf')
        """
        return FileResponse(buffer,
                            filename='report.pdf')


class IndexWeasyView(View):
    def get(self, request, *args, **kwargs):
        texto = ['Diego', 'Campos', 'Lima']
        html_string = render_to_string('relatorio.html',
                                       {
                                           'texto': texto
                                       })
        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/report_weasy.pdf')
        fs = FileSystemStorage('/tmp')
        with fs.open('report_weasy.pdf') as pdf:
            response = HttpResponse(pdf,
                                    content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="report_weasy.pdf"'
        return response
