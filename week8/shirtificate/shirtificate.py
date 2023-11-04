from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font(family="helvetica", style="", size=48)
        self.cell(0, 60, "CS50 Shirtificate", align="C")
        self.ln(20)
        self.image("./shirtificate.png", 15, 70, 180)


def main():
    name = input("Name: ")
    create_shirt(name)


def create_shirt(name):
    pdf = PDF()
    pdf.add_page(orientation="portrait", format="a4")
    pdf.set_font(family="helvetica", size=24)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 200, f"{name} took CS50", align="C")
    pdf.set_auto_page_break(auto=False)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
