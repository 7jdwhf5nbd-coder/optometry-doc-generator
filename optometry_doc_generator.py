import csv
import re
from datetime import datetime
from reportlab.lib.pagesizes import A4, letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfgen import canvas
import os
import tkinter as tk
from tkinter import ttk, messagebox
from PyPDF2 import PdfReader, PdfWriter
import io
import sys

# --- AUTO-DETECT BASE DIRECTORY (WORKS ON NETWORK, USB, OR LOCAL) ---
if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# --- FILE PATHS ---
CSV_FILE_PATH = os.path.join(BASE_DIR, "doctors_list-2.csv")
LETTERHEAD_IMAGE = os.path.join(BASE_DIR, "letterhead.png")

# Clinic details
CLINIC_NAME = "Bancroft Eye Care"
CLINIC_ADDRESS = "225 Hastings St. N., PO Box 820, Bancroft, ON K0L 1C0"
CLINIC_PHONE = "613-332-1234"
CLINIC_FAX = "613-332-9959"
CLINIC_WEBSITE = "www.bancrofteyecare.com"

# Signature options
SIGNATURES = ["J. Rawal, O.D.", "J. Guthrie, O.D.", "None"]

# [Rest of your code — unchanged except template paths below]
# In generate_diabetes_report():
template_path = os.path.join(BASE_DIR, "DM Form.pdf")

# In generate_mto_report():
mto_template = os.path.join(BASE_DIR, "MTO JR.pdf") if "Rawal" in signature else os.path.join(BASE_DIR, "MTO JG.pdf")