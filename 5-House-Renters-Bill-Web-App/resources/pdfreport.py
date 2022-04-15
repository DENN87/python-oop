from fpdf import FPDF


class PdfReport:
    """
    Creates a PDF file that contains data about
    the house mates such as their names, their
    due amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate_pdf(self, renters_list, bill):
        pdf = FPDF(orientation='P', unit='pt', format='letter')
        pdf.add_page()
        pdf.set_fill_color(228, 233, 190)

        # Adding a image
        pdf.image(name="files/house.png", x=532, y=40, w=50, h=50)

        # Insert Line
        pdf.set_line_width(2)
        pdf.line(30, 30, 582, 30)
        pdf.set_line_width(0)

        # Insert title
        pdf.set_font(family='Helvetica', size=24, style='B')
        pdf.cell(w=0, h=80, txt="HOUSE RENTAL INVOICE", border=0, align="L", ln=1)

        # Insert Invoice Number & Period
        pdf.set_left_margin(382)
        pdf.set_font(family='Helvetica', size=12, style='B')
        pdf.cell(w=100, h=20, txt="Invoice #", border=1, align="L", fill=1)
        pdf.set_font(family='Helvetica', size=12)
        pdf.cell(w=100, h=20, txt="1000003", border=1, align="L", ln=1)
        pdf.set_font(family='Helvetica', size=12, style='B')
        pdf.cell(w=100, h=20, txt="Invoice date", border=1, align="L", fill=1)
        pdf.set_font(family='Helvetica', size=12)
        pdf.cell(w=100, h=20, txt=bill.period, border=1, align="L", ln=1)
        pdf.set_left_margin(28.35)
        pdf.ln()

        # Insert Line
        pdf.set_line_width(2)
        pdf.line(30, 220, 582, 220)
        pdf.set_line_width(0)

        # PDF Body
        pdf.ln()
        pdf.ln()
        pdf.ln()
        pdf.ln()

        # Define cell column names
        pdf.set_font(family='Helvetica', size=12, style='B')
        pdf.cell(w=100, h=20, txt="Renter Name", border=1, align="C", fill=1)
        pdf.cell(w=250, h=20, txt="Room Description", border=1, align="C", fill=1)
        pdf.cell(w=100, h=20, txt="Days Rented", border=1, align="C", fill=1)
        pdf.cell(w=0, h=20, txt="Total ($)", border=1, align="C", fill=1, ln=1)

        # Insert Renters details
        for renter in renters_list:
            pdf.set_font(family='Helvetica', size=12, style='I')
            pdf.cell(w=100, h=20, txt=renter.name, border=1, align="C")
            pdf.cell(w=250, h=20, txt="Shared House", border=1, align="C")
            pdf.cell(w=100, h=20, txt=str(renter.days_in_house), border=1, align="C")
            pdf.cell(w=0, h=20, txt=str(renter.pays(bill, renters_list)), border=1, align="C", ln=1)

        # Total Bill amount
        pdf.set_font(family='Helvetica', size=12, style='B')
        pdf.cell(w=100, h=20, txt="", border=0, align="C")
        pdf.cell(w=250, h=20, txt="", border=0, align="C")
        pdf.cell(w=100, h=20, txt="Total ($)", border=1, align="C", fill=1)
        pdf.cell(w=0, h=20, txt=str(bill.amount), border=1, align="C", fill=1, ln=1)

        # Write to file
        pdf.output(self.filename)


from filestack import Client


class FileShare:
    # Get api_key from www.filestack.com and added to api_key="<key>"

    def __init__(self, filepath, api_key="<your_key>"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        """Uploads the filename from file_path to the filestack.com
        and returns the url of the image"""

        client = Client(self.api_key)
        new_file_link = client.upload(filepath=self.filepath)
        return new_file_link.url

