from fpdf import FPDF

def generate_pdf_report(user_name, health_data, health_risk, filename="Health_Report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt=f"Health Report for {user_name}", ln=True, align='C')
    pdf.ln(10)

    for key, value in health_data.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Predicted Health Risk Level: {health_risk}", ln=True, align='L')

    pdf.output(filename)
    print(f"PDF report generated: {filename}")

# Example usage:
# Define some example data and a risk level
health_data = {"Heart Rate": 72, "Steps": 8500, "Sleep Quality": "Good"}
risk = "Low"
generate_pdf_report("John Doe", health_data, risk)