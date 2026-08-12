import streamlit as st
import requests
import re

# Mobile Visual Configuration Layout
st.set_page_config(page_title="Spicen Tech Intel", page_icon="⚡", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #F4F7F9; }
    .stButton>button { width: 100%; background-color: #1C2D42; color: white; font-weight: bold; border-radius: 8px; height: 3em;}
    .report-box { background-color: #FFFFFF; padding: 20px; border-radius: 8px; border-left: 5px solid #1C2D42; margin-bottom: 15px; }
    h1, h2, h3 { color: #1C2D42; font-family: 'Segoe UI', sans-serif; }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ SPICEN TECHNOLOGIES")
st.subheader("Universal ECE Architectural Engine v6.3")
st.write("Professional Engineering Field Lab Report Tool")

# ==============================================================================
# INDUSTRIAL MULTI-LAYER TECHNICAL RESOLVER
# ==============================================================================
def deep_ece_hardware_extractor(user_input):
    raw_query = user_input.strip()
    if not raw_query:
        return None
        
    upper_query = raw_query.upper().split('/')[0]
    clean_chip = re.sub(r'(BEX\d|NOPB|G$|E4$)', '', upper_query)
    formatted_word = raw_query.title() if raw_query.islower() else raw_query
    
    # Base Data Extraction Variable
    web_summary = ""
    headers = {"User-Agent": "SpicenTechMobileEngine/6.0 (host@spicentech.com)"}
    
    # Attempt live structural data extraction from parent silicon tree indexes
    for term in [clean_chip, formatted_word]:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{term.replace(' ', '_')}"
        try:
            response = requests.get(url, headers=headers, timeout=4)
            if response.status_code == 200:
                web_summary = response.json().get("extract", "")
                if web_summary:
                    break
        except:
            pass

    # ==============================================================================
    # ALGORITHMIC LAB PARAMETER SYNTHESIZER
    # This matrix evaluates part numbers or words against ECE industry rules to map specifications
    # ==============================================================================
    
    # Default State Initializers
    component_identity = raw_query
    classification = "Specialized Integrated Circuit / Device Asset"
    purpose = "Utilized for complex conditioning or custom logic manipulation within custom circuit grids."
    how_to_use = "1. Align the chip notch pointing left or up to map the Pin 1 layout standard.\n2. Apply appropriate operating voltages to designated power pins.\n3. Route input signal pins through filtering capacitors to minimize data line bounce."
    typical_circuits = "Signal isolation paths, customized embedded computing controllers, or specialized breadboard test fixtures."
    key_specs = "• Operating Voltage: Varies by manufacturer sub-type variant\n• Pin Mapping: Standard DIP or surface-mount orientation configurations\n• Thermal Limit: Built-in protective junction scaling threshold"

    # Context Analysis Keywords
    desc_check = web_summary.lower() if web_summary else ""
    
    # DYNAMIC LOGIC ROUTER 1: AMPLIFIERS & OP-AMPS (e.g., LM3886, LM358, TL072)
    if "amplifier" in desc_check or "op-amp" in desc_check or clean_chip.startswith("LM") and any(x in clean_chip for x in ["388", "358", "324", "741"]) or clean_chip.startswith("TL"):
        classification = "Analog: Operational / Power Amplifier Module"
        purpose = "Designed to boost weak input electrical voltages or audio wave alternating currents up to standard usable voltage thresholds without altering input structural frequencies."
        how_to_use = "1. Power with a single or split balanced rail source (e.g., +15V and -15V connected to power rails).\n2. Connect the non-inverting input pin (+) to the reference line or clean source signal.\n3. Place a feedback resistor connection bridging the output pin back to the inverting input pin (-) to control specific feedback amplification gains."
        typical_circuits = "Audio pre-amplifier stages, sensor output voltage buffers, instrumentation mixers, and active analog filtering matrix networks."
        key_specs = "• Voltage Range: Typically ±3V up to ±22V or higher\n• Input Impedance: High input isolation to prevent source loading\n• Output Current Protection: Internal short-circuit current limit clamping thresholds"
        if "3886" in clean_chip:
            component_identity = "LM3886 High-Performance Audio Power Amplifier"
            purpose = "High-fidelity Overture audio amplification component capable of driving heavy speaker loads directly."
            key_specs = "• Continuous Output Power: 68W into 4 Ohms\n• Total Harmonic Distortion: 0.03% typ\n• Power Supply Range: 20V to 84V"

    # DYNAMIC LOGIC ROUTER 2: DIGITAL LOGIC GATES (e.g., 7408, 7432, CD4017)
    elif "logic" in desc_check or "gate" in desc_check or clean_chip.startswith("74") or clean_chip.startswith("CD"):
        classification = "Digital: Transistor-Transistor Logic (TTL) / CMOS Gating Network"
        purpose = "Executes immediate conditional computing calculations by managing binary high/low (1 or 0) electrical states across transistor micro-arrays."
        how_to_use = "1. Supply a steady, precise +5V (for 74-series TTL) or up to +15V (for CD4000 CMOS series) to the VCC/VDD pin, and tie the opposite power pin directly to lab ground.\n2. Send binary logic inputs using digital signal controllers or manual pull-up switches.\n3. Connect output pins directly to downstream logic chips or to an LED utilizing an inline current-limiting tracking resistor."
        typical_circuits = "Arithmetic Logic Units (ALUs), hardware state machine triggers, control clock lines, debounced signal routing gates."
        key_specs = "• Logic High Threshold: >2.0V minimum (TTL layout environments)\n• Propagation Delay Time: Measured in nanoseconds per internal logic gate stage\n• Max Static Current Draw: Micro-amp metrics per logic cell block"

    # DYNAMIC LOGIC ROUTER 3: EMBEDDED PROCESSORS & MICROCONTROLLERS (e.g., ATMEGA, STM32, ESP32)
    elif "microcontroller" in desc_check or "processor" in desc_check or any(x in clean_chip for x in ["ATM", "STM", "ESP", "PIC"]):
        classification = "Embedded Systems: Programmable Core Microprocessor / System on Chip"
        purpose = "Serves as the central control processor. Reads hardware tracking sensors, calculates logic steps, and outputs automated commands based on custom firmware code."
        how_to_use = "1. Connect an external clock oscillator crystal if required by the sub-core layout.\n2. Power cleanly using decoupled 3.3V or 5V voltage regulators to insulate from noise spikes.\n3. Flash your software control loops through standard USB-UART programming pins."
        typical_circuits = "Robotics controllers, custom IoT sensor nodes, home automation modules, smart embedded appliances."
        key_specs = "• Core Architecture Clock Speed: 8MHz up to 240MHz+\n• Dynamic Storage Layout: Internal Flash memory alongside RAM structures\n• Communication Protocol Buses: Integrated hardware SPI, I2C, and UART peripherals"

    # DYNAMIC LOGIC ROUTER 4: VOLTAGE REFERENCES & REGULATORS (e.g., LM4041, LM7805, TL431)
    elif "reference" in desc_check or "regulator" in desc_check or "shunt" in desc_check or "4041" in clean_chip or clean_chip.startswith("78"):
        classification = "Power Management: Precision Voltage Reference / Regulator Architecture"
        purpose = "Generates a rock-solid, fixed reference voltage level that remains steady despite spikes in the raw input power lines."
        how_to_use = "1. If configuring a shunt reference like the LM4041, supply current through an input resistor to keep the device operating within its breakdown curve.\n2. Route the output trace through a ceramic capacitor located close to the pin structure to scrub out alternating current ripple noise.\n3. Route the reference line directly to the Analog-to-Digital Converter reference pin."
        typical_circuits = "Precision sensor scale calibration systems, Analog-to-Digital conversion pipelines, power supply feedback networks."
        key_specs = "• Target Output Accuracy: Precision tolerances down to 0.1%\n• Maximum Current Handling Capacity: Varies depending on shunt or series layout topology\n• Temperature Drift Coefficient: Monitored in parts per million per degree Celsius"

    # DYNAMIC LOGIC ROUTER 5: FUNDAMENTAL PASSIVE PASS COMPONENT WORDS (e.g., Capacitor, Resistor, Diode)
    elif "capacitor" in desc_check or "capacitance" in desc_check or formatted_word == "Capacitor":
        classification = "Passive Component: Electrostatic Energy Field Capacitor"
        purpose = "Temporarily stores electrical energy within an internal electrostatic field while acting as a barrier to direct current and a clean pathway for alternating current signals."
        how_to_use = "1. Double-check device polarization markers if deploying electrolytic variations (incorrect connection will burst the canister structure).\n2. Place parallel decoupling capacitors directly against integrated circuit power input pins to eliminate supply line voltage dips.\n3. Pair with standard resistors to create custom RC timing circuits."
        typical_circuits = "Power supply ripples smoothers, audio amplifier coupling nodes, noise frequency filtering networks."
        key_specs = "• Capacitance Scale: Measured from picofarads (pF) up to microfarads (uF)\n• Max Voltage Breakdown: Peak operating envelope ceiling before structural dielectric failure\n• ESR Rating: Equivalent Series Resistance efficiency metrics"

    # If web summary was found but didn't match a specialized category rule, enrich generic description
    if web_summary and purpose == "Utilized for complex conditioning or custom logic manipulation within custom circuit grids.":
        purpose = web_summary

    return {
        "name": raw_query.upper(),
        "class": classification,
        "purpose": purpose,
        "usage": how_to_use,
        "circuits": typical_circuits,
        "specs": key_specs
    }

# ==============================================================================
# STREAMLIT MOBILE INTERFACE GRID DISPLAY
# ==============================================================================
user_input = st.text_input("Enter Any Part Number, Concept, or IC Code (e.g., LM3886T/NOPB, 7408, Capacitor, LM4041BEX3):", value="LM3886T/NOPB")

if st.button("Generate Complete Lab Report"):
    if user_input:
        with st.spinner("Extracting parameters across global silicon records..."):
            report = deep_ece_hardware_extractor(user_input)
            
        if report:
            st.success(f"### 📊 FIELD ANALYSIS REPORT: {report['name']}")
            
            # Category Banner Card View
            st.markdown(f"""
            <div class='report-box'>
                <h4>🧬 ECE Classification Group</h4>
                <p><strong>{report['class']}</strong></p>
            </div>
            """, unsafe_allow_html=True)
            
            # Core Parameters Accordion System (Optimized for scrolling cleanly on mobile screen layout displays)
            with st.expander("🔍 1. What Is It & General Purpose?", expanded=True):
                st.write(report['purpose'])
                
            with st.expander("🛠️ 2. How Is It Used? (Lab Implementation Guide)", expanded=True):
                st.write(report['usage'])
                
            with st.expander("🔌 3. Core Electrical Specifications & Metrics", expanded=True):
                st.markdown(report['specs'])
                
            with st.expander("📋 4. Common Application & Target Lab Circuits", expanded=True):
                st.write(report['circuits'])
                
            st.caption("Engine System Status: Operational 24/7 | Spicen Technologies Academic Framework Pipeline")