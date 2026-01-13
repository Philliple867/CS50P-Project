from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Set font for the header
        self.set_font("helvetica", "B", 45)
        # Move to the center and print title
        self.cell(0, 60, "CS50 Shirtificate", align="C", ln=True)

def main():
    name = input("Name: ")
    create_shirt(name)

def create_shirt(name):
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Place the shirt image: center it horizontally
    # Image width is 190mm (A4 is 210mm wide)
    pdf.image("shirtificate.png", x=10, y=70, w=190)

    # Set font for the name on the shirt
    pdf.set_font("helvetica", "B", 25)
    pdf.set_text_color(255, 255, 255) # White color

    # Move to the position on the shirt and print name
    pdf.cell(0, 140, f"{name} took CS50", align="C")

    # Output the final PDF
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
