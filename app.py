#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 19:48:33 2025
By Eric Espinosa

Merged Application for Lakes HOA (Painting, Remodel, Roofing, Solar)
"""
import streamlit as st
import io
from datetime import date
from pypdf import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# --- 1. CONFIGURATION (MUST BE FIRST) ---
st.set_page_config(page_title="Lakes HOA Portal", page_icon="🏡")

# FILENAMES
PAINT_PDF = "ACC-Application-Painting-November-2023.pdf"
REMODEL_PDF = "ACC-Application-Remodels-Strucures-Landscape-June-2024.pdf"
ROOFING_PDF = "ACC-Application-Roofing-November-2023.pdf"
SOLAR_PDF = "ACC-Application-Solar-Energy-Panel-November-2023.pdf"

# ==========================================
# 2. HELPER FUNCTIONS
# ==========================================
def draw_helper(can, data, x, y, key):
    """Simple helper to check if key exists before drawing"""
    if data.get(key): 
        can.drawString(x, y, str(data.get(key)))

def check_helper(can, data, x, y, key):
    """Draws an X if the boolean key is True"""
    if data.get(key): 
        can.drawString(x, y, "X")

# ==========================================
# 3. OVERLAY ENGINES
# ==========================================

def create_painting_overlay(data):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont("Helvetica", 10)
    
    # --- PAGE 1 (Matches PDF Page 2) ---
    draw_helper(can, data, 170, 670, "date_prepared") 
    draw_helper(can, data, 170, 653, "owner_name")   
    draw_helper(can, data, 425, 653, "lot_number")   
    draw_helper(can, data, 170, 635, "address")      
    draw_helper(can, data, 170, 607, "designated_contact")
    
    draw_helper(can, data, 170, 578, "home_phone")   
    draw_helper(can, data, 425, 578, "work_phone")   
    draw_helper(can, data, 170, 565, "mobile_phone") 
    draw_helper(can, data, 425, 565, "email")        
    
    draw_helper(can, data, 170, 550, "start_date")   
    draw_helper(can, data, 425, 550, "end_date")     

    draw_helper(can, data, 150, 295, "contractor_name")
    draw_helper(can, data, 150, 280, "contractor_address")
    draw_helper(can, data, 150, 268, "contractor_phone")

    # Paint Table
    draw_helper(can, data, 160, 178, "siding_mfg"); draw_helper(can, data, 250, 178, "siding_id"); draw_helper(can, data, 400, 178, "siding_name")
    draw_helper(can, data, 160, 164, "brickwork_mfg"); draw_helper(can, data, 250, 164, "brickwork_id"); draw_helper(can, data, 400, 164, "brickwork_name")
    draw_helper(can, data, 160, 152, "trim_mfg"); draw_helper(can, data, 250, 152, "trim_id"); draw_helper(can, data, 400, 152, "trim_name")
    draw_helper(can, data, 160, 137, "shutter_mfg"); draw_helper(can, data, 250, 137, "shutter_id"); draw_helper(can, data, 400, 137, "shutter_name")
    draw_helper(can, data, 160, 125, "door_mfg"); draw_helper(can, data, 250, 125, "door_id"); draw_helper(can, data, 400, 125, "door_name")
    draw_helper(can, data, 160, 110, "fence_mfg"); draw_helper(can, data, 250, 110, "fence_id"); draw_helper(can, data, 400, 110, "fence_name")
    draw_helper(can, data, 160, 98, "other_mfg"); draw_helper(can, data, 400, 98, "other_color_name") 

    can.showPage() 

    # --- PAGE 2 (Samples) ---
    if data.get("samples_status") == "Samples Placed":
        can.drawString(45, 645, "X") 
        draw_helper(can, data, 60, 630, "samples_location") 
    elif data.get("samples_status") == "Email ACC":
        can.drawString(45, 612, "X")

    can.save()
    packet.seek(0)
    return packet

def create_remodel_overlay(data):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont("Helvetica", 10)
    
    # --- PAGE 1 OF OVERLAY ---
    draw_helper(can, data, 170, 625, "date_prepared")
    draw_helper(can, data, 170, 610, "owner_name")
    draw_helper(can, data, 425, 610, "lot_number")
    draw_helper(can, data, 170, 587, "address")
    draw_helper(can, data, 170, 555, "designated_contact")
    
    draw_helper(can, data, 170, 534, "home_phone")
    draw_helper(can, data, 425, 534, "work_phone")
    draw_helper(can, data, 170, 520, "mobile_phone")
    draw_helper(can, data, 425, 520, "email")
    
    draw_helper(can, data, 170, 505, "start_date")
    draw_helper(can, data, 425, 505, "end_date")
    
    draw_helper(can, data, 150, 330, "contractor_name")
    draw_helper(can, data, 150, 317, "contractor_address")
    draw_helper(can, data, 150, 304, "contractor_phone")

    # Remodel Checkboxes
    check_helper(can, data, 170, 225, "rem_room"); check_helper(can, data, 170, 215, "rem_win"); check_helper(can, data, 170, 202, "rem_mason")
    check_helper(can, data, 290, 225, "rem_deck"); check_helper(can, data, 290, 215, "rem_cover"); check_helper(can, data, 290, 202, "rem_planter")
    check_helper(can, data, 445, 225, "rem_drive"); check_helper(can, data, 445, 215, "rem_retain")
    
    can.showPage() 

    # --- PAGE 2 OF OVERLAY ---
    # Structures
    check_helper(can, data, 185, 695, "str_fence"); check_helper(can, data, 185, 675, "str_bbq"); check_helper(can, data, 185, 660, "str_ac")
    check_helper(can, data, 185, 645, "str_gen"); check_helper(can, data, 185, 630, "str_swing")
    check_helper(can, data, 300, 695, "str_pool"); check_helper(can, data, 300, 675, "str_gazebo"); check_helper(can, data, 300, 660, "str_trellis")
    check_helper(can, data, 300, 645, "str_hoop"); check_helper(can, data, 300, 630, "str_gym")
    check_helper(can, data, 425, 695, "str_wall"); check_helper(can, data, 425, 675, "str_green"); check_helper(can, data, 425, 660, "str_shed")
    check_helper(can, data, 425, 645, "str_play"); check_helper(can, data, 425, 630, "str_tramp")

    # Landscape
    check_helper(can, data, 180, 505, "lnd_grade"); check_helper(can, data, 180, 485, "lnd_art")
    check_helper(can, data, 330, 505, "lnd_retain"); check_helper(can, data, 330, 485, "lnd_tree_rem")
    check_helper(can, data, 495, 505, "lnd_shrub"); check_helper(can, data, 495, 485, "lnd_conserv")

    can.save()
    packet.seek(0)
    return packet

def create_roofing_overlay(data):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont("Helvetica", 10)
    
    # --- PAGE 1 OF OVERLAY (Matches PDF Page 2) ---
    draw_helper(can, data, 190, 678, "owner_name")
    draw_helper(can, data, 440, 650, "lot_number")
    draw_helper(can, data, 190, 662, "address")
    draw_helper(can, data, 190, 650, "date_prepared") 

    draw_helper(can, data, 190, 635, "home_phone")
    draw_helper(can, data, 440, 635, "work_phone")
    draw_helper(can, data, 190, 620, "mobile_phone")
    draw_helper(can, data, 440, 620, "email")
    
    draw_helper(can, data, 190, 605, "start_date")
    draw_helper(can, data, 440, 605, "end_date")
    
    # Logic for Contractor Sections
    roof_action = data.get("roof_action")
    
    if roof_action == "Replacement":
        # General/Replacement Contractor (Top Box)
        draw_helper(can, data, 200, 540, "contractor_name")
        draw_helper(can, data, 200, 525, "contractor_address")
        draw_helper(can, data, 200, 515, "contractor_phone")
        
    elif roof_action == "Cleaning":
        # Cleaning Contractor (Middle Box)
        draw_helper(can, data, 200, 465, "contractor_name")
        draw_helper(can, data, 200, 450, "contractor_address")
        draw_helper(can, data, 200, 438, "contractor_phone")
        draw_helper(can, data, 200, 425, "roof_clean_product") 
        
    elif roof_action == "Tinting":
        # Tinting (Bottom Box)
        draw_helper(can, data, 60, 360, "roof_tint_mfg")
        draw_helper(can, data, 150, 360, "roof_tint_id")
        draw_helper(can, data, 290, 360, "roof_tint_name")

    can.save()
    packet.seek(0)
    return packet

def create_solar_overlay(data):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont("Helvetica", 10)
    
    # --- PAGE 1 OF OVERLAY (Matches Solar PDF Page 2) ---
    # VERIFIED USER COORDINATES
    draw_helper(can, data, 190, 620, "owner_name")
    draw_helper(can, data, 420, 588, "lot_number")
    draw_helper(can, data, 190, 604, "address")
    draw_helper(can, data, 190, 588, "date_prepared") 

    draw_helper(can, data, 190, 575, "home_phone")
    draw_helper(can, data, 420, 575, "work_phone")
    draw_helper(can, data, 190, 560, "mobile_phone")
    draw_helper(can, data, 420, 560, "email")
    
    draw_helper(can, data, 190, 540, "start_date")
    draw_helper(can, data, 420, 540, "end_date")
    
    # Contractor Section (Solar)
    draw_helper(can, data, 190, 490, "contractor_name")
    draw_helper(can, data, 190, 477, "contractor_address")
    draw_helper(can, data, 190, 460, "contractor_phone")

    can.save()
    packet.seek(0)
    return packet

# ==========================================
# 4. PDF GENERATION LOGIC
# ==========================================
def generate_final_pdf(data, form_type):
    start_page_idx = 1 # All forms currently start on Page 2 (Index 1)
    
    if form_type == "Painting":
        overlay = create_painting_overlay(data)
        src = PAINT_PDF
    elif form_type == "Remodel":
        overlay = create_remodel_overlay(data)
        src = REMODEL_PDF
    elif form_type == "Roofing":
        overlay = create_roofing_overlay(data)
        src = ROOFING_PDF
    elif form_type == "Solar":
        overlay = create_solar_overlay(data)
        src = SOLAR_PDF

    new_pdf = PdfReader(overlay)
    existing_pdf = PdfReader(open(src, "rb"))
    output = PdfWriter()

    # Add Instructions (Page 1)
    output.add_page(existing_pdf.pages[0])
    
    # Merge Page 1 of Overlay -> Form Page (Page 2)
    page_form = existing_pdf.pages[start_page_idx]
    if len(new_pdf.pages) > 0:
        page_form.merge_page(new_pdf.pages[0])
    output.add_page(page_form)

    # Merge Page 2 of Overlay -> Next Page (If needed for Remodel/Paint)
    if form_type in ["Remodel", "Painting"]:
        page_next = existing_pdf.pages[start_page_idx + 1]
        if len(new_pdf.pages) > 1:
            page_next.merge_page(new_pdf.pages[1])
        output.add_page(page_next)
    else:
        # Roofing/Solar don't have a second overlay page usually
        # But we need to add the actual PDF page if it exists
        if start_page_idx + 1 < len(existing_pdf.pages):
             output.add_page(existing_pdf.pages[start_page_idx + 1])

    # Add remaining pages
    start_rest = start_page_idx + 2 if form_type in ["Remodel", "Painting"] else start_page_idx + 2
    for i in range(start_rest, len(existing_pdf.pages)):
        output.add_page(existing_pdf.pages[i])

    return output

# ==========================================
# 5. STREAMLIT UI
# ==========================================
st.title("🏡 The Lakes HOA Application Portal")

# Sidebar for Navigation
app_mode = st.sidebar.selectbox("Select Application Type", 
    ["Exterior Painting", "Remodel / Structure / Landscape", "Roofing", "Solar Energy Panel"])

# --- COMMON FIELDS ---
st.subheader("1. Homeowner Information")
c1, c2 = st.columns(2)
owner_name = c1.text_input("Name")
lot_number = c2.text_input("Lot Number")
address = st.text_input("Address")
designated_contact = st.text_input("Designated Contact (if different)")

c3, c4 = st.columns(2)
home_phone = c3.text_input("Home Phone")
email = c4.text_input("Email")

st.subheader("2. Project Timeline")
c5, c6 = st.columns(2)
start_date = c5.date_input("Proposed Start Date")
end_date = c6.date_input("Est. Completion Date")

# --- APP SPECIFIC UI ---
form_data = {}

# === EXTERIOR PAINTING UI ===
if app_mode == "Exterior Painting":
    st.subheader("3. Contractor Information")
    c7, c8 = st.columns(2)
    contractor_name = c7.text_input("Contractor Name")
    contractor_phone = c8.text_input("Contractor Phone")
    contractor_address = st.text_input("Contractor Address")

    st.header("🎨 Painting Details")
    mfg_options = ["Benjamin Moore", "Sherwin Williams", "Miller", "Other"]

    st.markdown("**Siding**")
    r1c1, r1c2, r1c3 = st.columns(3)
    siding_mfg = r1c1.selectbox("Siding Manufacturer", mfg_options, index=None, placeholder="Select...")
    siding_id = r1c2.text_input("Color ID", key="s_id")
    siding_name = r1c3.text_input("Color Name", key="s_name")

    st.markdown("**Window Trim**")
    r2c1, r2c2, r2c3 = st.columns(3)
    trim_mfg = r2c1.selectbox("Trim Manufacturer", mfg_options, index=None, placeholder="Select...")
    trim_id = r2c2.text_input("Color ID", key="t_id")
    trim_name = r2c3.text_input("Color Name", key="t_name")

    st.markdown("**Brickwork Trim**")
    r3c1, r3c2, r3c3 = st.columns(3)
    brickwork_mfg = r3c1.selectbox("Brickwork Manufacturer", mfg_options, index=None, placeholder="Select...")
    brickwork_id = r3c2.text_input("Color ID", key="b_id")      
    brickwork_name = r3c3.text_input("Color Name", key="b_name") 

    st.markdown("**Shutters**")
    r4c1, r4c2, r4c3 = st.columns(3)
    shutter_mfg = r4c1.selectbox("Shutter Manufacturer", mfg_options, index=None, placeholder="Select...")
    shutter_id = r4c2.text_input("Color ID", key="sh_id")    
    shutter_name = r4c3.text_input("Color Name", key="sh_name") 

    st.markdown("**Front Door**")
    r5c1, r5c2, r5c3 = st.columns(3)
    door_mfg = r5c1.selectbox("Front Door Manufacturer", mfg_options, index=None, placeholder="Select...")
    door_id = r5c2.text_input("Color ID", key="d_id")      
    door_name = r5c3.text_input("Color Name", key="d_name") 

    st.markdown("**Fence**")
    r6c1, r6c2, r6c3 = st.columns(3)
    fence_mfg = r6c1.selectbox("Fence", mfg_options, index=None, placeholder="Select...")
    fence_id = r6c2.text_input("Color ID", key="f_id")      
    fence_name = r6c3.text_input("Color Name", key="f_name") 

    st.markdown("**Other Items**")
    c_other1, c_other2 = st.columns(2)
    other_mfg = c_other1.text_input("Other Item Manufacturer")
    other_color_name = c_other2.text_input("Other Item Color Name")

    st.subheader("5. Samples")
    samples_status = st.radio("Sample Status", ["Samples Placed", "Email ACC"], index=None)
    samples_location = ""
    if samples_status == "Samples Placed":
        samples_location = st.text_input("Where are the samples located? (e.g. Front Porch)")

    form_data.update({
        "contractor_name": contractor_name, "contractor_address": contractor_address, "contractor_phone": contractor_phone,
        "siding_mfg": siding_mfg, "siding_id": siding_id, "siding_name": siding_name,
        "brickwork_mfg": brickwork_mfg, "brickwork_id": brickwork_id, "brickwork_name": brickwork_name,
        "trim_mfg": trim_mfg, "trim_id": trim_id, "trim_name": trim_name,
        "shutter_mfg": shutter_mfg, "shutter_id": shutter_id, "shutter_name": shutter_name,
        "door_mfg": door_mfg, "door_id": door_id, "door_name": door_name,
        "fence_mfg": fence_mfg, "fence_id": fence_id, "fence_name": fence_name,
        "other_mfg": other_mfg, "other_color_name": other_color_name,
        "samples_status": samples_status, "samples_location": samples_location
    })

# === REMODEL UI ===
elif app_mode == "Remodel / Structure / Landscape":
    st.subheader("3. Contractor Information")
    c7, c8 = st.columns(2)
    contractor_name = c7.text_input("Contractor Name")
    contractor_phone = c8.text_input("Contractor Phone")
    contractor_address = st.text_input("Contractor Address")

    st.header("🔨 Project Details")
    
    with st.expander("External Home Remodel", expanded=True):
        c_r1, c_r2, c_r3 = st.columns(3)
        rem_room = c_r1.checkbox("Room Additions")
        rem_win = c_r1.checkbox("Windows/Doors")
        rem_mason = c_r1.checkbox("Masonry")
        rem_deck = c_r2.checkbox("Deck or Patio")
        rem_cover = c_r2.checkbox("Patio Cover")
        rem_planter = c_r2.checkbox("Attached Planter")
        rem_drive = c_r3.checkbox("Driveway Mod")
        rem_retain = c_r3.checkbox("Retaining Wall (Attached)")

    with st.expander("Free-Standing Structures"):
        c_s1, c_s2, c_s3 = st.columns(3)
        str_fence = c_s1.checkbox("New/Repl Fence")
        str_bbq = c_s1.checkbox("Outdoor Fireplace/BBQ")
        str_ac = c_s1.checkbox("AC Unit")
        str_gen = c_s1.checkbox("Generator")
        str_swing = c_s1.checkbox("Swing Set")
        str_pool = c_s2.checkbox("Spa or Pool")
        str_gazebo = c_s2.checkbox("Gazebo")
        str_trellis = c_s2.checkbox("Arbor or Trellis")
        str_hoop = c_s2.checkbox("Basketball Hoop")
        str_gym = c_s2.checkbox("Jungle Gym")
        str_wall = c_s3.checkbox("Masonry Wall")
        str_green = c_s3.checkbox("Greenhouse")
        str_shed = c_s3.checkbox("Garden Shed")
        str_play = c_s3.checkbox("Playhouse")
        str_tramp = c_s3.checkbox("Trampoline")

    with st.expander("Landscaping"):
        c_l1, c_l2, c_l3 = st.columns(3)
        lnd_grade = c_l1.checkbox("Lawn/Garden Grade Change")
        lnd_art = c_l1.checkbox("Artificial Turf")
        lnd_retain = c_l2.checkbox("Retaining Wall (Landscape)")
        lnd_tree_rem = c_l2.checkbox("Protected Tree Removal")
        lnd_shrub = c_l3.checkbox("Trees/Shrubs <20' of Lake")
        lnd_conserv = c_l3.checkbox("Conservancy Plant Removal")
        
    form_data.update({
        "contractor_name": contractor_name, "contractor_address": contractor_address, "contractor_phone": contractor_phone,
        "rem_room": rem_room, "rem_win": rem_win, "rem_mason": rem_mason,
        "rem_deck": rem_deck, "rem_cover": rem_cover, "rem_planter": rem_planter,
        "rem_drive": rem_drive, "rem_retain": rem_retain,
        "str_fence": str_fence, "str_bbq": str_bbq, "str_ac": str_ac,
        "str_gen": str_gen, "str_swing": str_swing,
        "str_pool": str_pool, "str_gazebo": str_gazebo, "str_trellis": str_trellis,
        "str_hoop": str_hoop, "str_gym": str_gym,
        "str_wall": str_wall, "str_green": str_green, "str_shed": str_shed,
        "str_play": str_play, "str_tramp": str_tramp,
        "lnd_grade": lnd_grade, "lnd_art": lnd_art,
        "lnd_retain": lnd_retain, "lnd_tree_rem": lnd_tree_rem,
        "lnd_shrub": lnd_shrub, "lnd_conserv": lnd_conserv
    })

# === ROOFING UI ===
elif app_mode == "Roofing":
    st.header("🏠 Roofing Details")
    
    roof_action = st.radio("Select Roofing Action", ["Replacement", "Cleaning", "Tinting"])
    
    if roof_action == "Replacement":
        st.info("Requirement: All replacement roofs shall utilize #1 sawn cedar shakes.")
        st.subheader("Contractor Information (Replacement)")
        contractor_name = st.text_input("Contractor Name")
        contractor_phone = st.text_input("Contractor Phone")
        contractor_address = st.text_input("Contractor Address")
        form_data.update({
            "contractor_name": contractor_name, "contractor_address": contractor_address, "contractor_phone": contractor_phone
        })
        
    elif roof_action == "Cleaning":
        st.subheader("Contractor Information (Cleaning)")
        contractor_name = st.text_input("Contractor Name")
        contractor_phone = st.text_input("Contractor Phone")
        contractor_address = st.text_input("Contractor Address")
        roof_clean_product = st.text_input("Product to be Used")
        form_data.update({
            "contractor_name": contractor_name, "contractor_address": contractor_address, "contractor_phone": contractor_phone,
            "roof_clean_product": roof_clean_product
        })
        
    elif roof_action == "Tinting":
        st.subheader("Tinting Specs")
        roof_tint_mfg = st.text_input("Manufacturer")
        roof_tint_id = st.text_input("Color ID Number")
        roof_tint_name = st.text_input("Color Name")
        form_data.update({
            "roof_tint_mfg": roof_tint_mfg, "roof_tint_id": roof_tint_id, "roof_tint_name": roof_tint_name
        })
        
    form_data.update({"roof_action": roof_action})

# === SOLAR UI ===
elif app_mode == "Solar Energy Panel":
    st.header("☀️ Solar Panel Details")
    
    st.subheader("3. Contractor / Installer")
    c7, c8 = st.columns(2)
    contractor_name = c7.text_input("Contractor Name")
    contractor_phone = c8.text_input("Contractor Phone")
    contractor_address = st.text_input("Contractor Address")
    
    st.subheader("4. Required Documents")
    st.info("Please attach these documents to your final email submission:")
    st.markdown("- **Drawings/Specifications**: Showing location, conduits, and compliance.")
    st.markdown("- **Aerial View**: Showing proposed panel on roof.")
    st.markdown("- **Manufacturer Specifications**: For the equipment.")
    
    form_data.update({
        "contractor_name": contractor_name, 
        "contractor_address": contractor_address, 
        "contractor_phone": contractor_phone
    })

# --- SUBMISSION ---
submitted = st.button("Generate Application PDF")

if submitted:
    # Bundle Common Data
    form_data.update({
        "date_prepared": date.today().strftime("%B %d, %Y"),
        "owner_name": owner_name, "lot_number": lot_number,
        "address": address, "designated_contact": designated_contact,
        "home_phone": home_phone, "email": email,
        "start_date": start_date, "end_date": end_date,
    })

    try:
        final_form_type = "Painting"
        if app_mode == "Remodel / Structure / Landscape": final_form_type = "Remodel"
        elif app_mode == "Roofing": final_form_type = "Roofing"
        elif app_mode == "Solar Energy Panel": final_form_type = "Solar"
        
        final_pdf = generate_final_pdf(form_data, final_form_type)
        out_buffer = io.BytesIO()
        final_pdf.write(out_buffer)
        
        st.success(f"✅ {app_mode} Generated!")
        st.download_button(
            label="⬇️ Download PDF",
            data=out_buffer.getvalue(),
            file_name=f"{app_mode.split()[0]}_App_{owner_name}.pdf",
            mime="application/pdf"
        )
    except FileNotFoundError as e:
        st.error(f"Error: {e}. Check your filenames!")
    except Exception as e:
        st.error(f"An error occurred: {e}")
