import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from interaction_diagram import generate_interaction_diagram
from materials import DesignCode

def validate_inputs():
    try:
        fc = float(fc_entry.get())
        fy = float(fy_entry.get())
        b = float(width_entry.get())
        h = float(depth_entry.get())
        rebar_layout = list(map(float, rebar_entry.get().split(',')))
        design_N = float(load_entry.get())
        design_M = float(moment_entry.get())
        code = DesignCode[code_var.get()]

        # Optional range checks
        if not (10 <= fc <= 100): raise ValueError("fc should be between 10 and 100 MPa")
        if not (200 <= fy <= 600): raise ValueError("fy should be between 200 and 600 MPa")
        if not rebar_layout: raise ValueError("Rebar layout cannot be empty")

        return fc, fy, b, h, rebar_layout, design_N, design_M, code
    except Exception as e:
        raise ValueError(f"Input error: {e}")

def run_analysis():
    try:
        fc, fy, b, h, rebar_layout, design_N, design_M, code = validate_inputs()
        fig, result = generate_interaction_diagram(fc, fy, b, h, rebar_layout, code, design_N, design_M)

        # Format diagram
        ax = fig.axes[0]
        ax.set_xlabel("Axial Load [kN]")
        ax.set_ylabel("Moment [kNm]")
        ax.set_title("Interaction Diagram")

        # Display diagram
        update_canvas(fig)

        # Summary popup
        summary = (
            f"Axial Load Check: {'✓ PASS' if result['passes_N'] else '✗ FAIL'}\n"
            f"Moment Check: {'✓ PASS' if result['passes_M'] else '✗ FAIL'}\n\n"
            f"N Capacity = {result['capacity_N'] / 1000:.1f} kN\n"
            f"M Capacity = {result['capacity_M'] / 1e6:.2f} kNm"
        )
        messagebox.showinfo("Validation Summary", summary)

    except Exception as e:
        messagebox.showerror("Analysis Error", str(e))

def export_results():
    try:
        fc, fy, b, h, rebar_layout, design_N, design_M, code = validate_inputs()
        fig, result = generate_interaction_diagram(fc, fy, b, h, rebar_layout, code, design_N, design_M)

        # Save text summary
        with open("rc_analysis_summary.txt", "w") as f:
            f.write("RC Section Analysis Summary\n")
            f.write("===========================\n")
            f.write(f"Design Code: {code.name}\n")
            f.write(f"fc = {fc} MPa, fy = {fy} MPa\n")
            f.write(f"Section Size: {b} mm × {h} mm\n")
            f.write(f"Rebar Layout: {rebar_layout}\n")
            f.write(f"Design Load: {design_N / 1000:.1f} kN\n")
            f.write(f"Design Moment: {design_M / 1e6:.2f} kNm\n")
            f.write(f"\nAxial Load Check: {'PASS' if result['passes_N'] else 'FAIL'}\n")
            f.write(f"Moment Check: {'PASS' if result['passes_M'] else 'FAIL'}\n")
            f.write(f"N Capacity = {result['capacity_N'] / 1000:.1f} kN\n")
            f.write(f"M Capacity = {result['capacity_M'] / 1e6:.2f} kNm\n")

        fig.savefig("rc_interaction_diagram.png", dpi=150)
        messagebox.showinfo("Export Complete", "Diagram and summary saved!")

    except Exception as e:
        messagebox.showerror("Export Error", str(e))

def update_canvas(fig):
    global canvas
    if canvas:
        canvas.get_tk_widget().destroy()
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# ---- UI Layout ----
root = tk.Tk()
root.title("RC Section Designer")
root.geometry("900x700")

input_frame = ttk.Frame(root, padding=10)
input_frame.pack(side=tk.LEFT, fill=tk.Y)

plot_frame = ttk.Frame(root, padding=10)
plot_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Input fields
ttk.Label(input_frame, text="Concrete strength fc (MPa):").pack()
fc_entry = ttk.Entry(input_frame); fc_entry.pack()

ttk.Label(input_frame, text="Steel strength fy (MPa):").pack()
fy_entry = ttk.Entry(input_frame); fy_entry.pack()

ttk.Label(input_frame, text="Section width b (mm):").pack()
width_entry = ttk.Entry(input_frame); width_entry.pack()

ttk.Label(input_frame, text="Section depth h (mm):").pack()
depth_entry = ttk.Entry(input_frame); depth_entry.pack()

ttk.Label(input_frame, text="Rebar layout (comma-separated, mm):").pack()
rebar_entry = ttk.Entry(input_frame); rebar_entry.pack()

ttk.Label(input_frame, text="Design axial load N (N):").pack()
load_entry = ttk.Entry(input_frame); load_entry.pack()

ttk.Label(input_frame, text="Design moment M (N·mm):").pack()
moment_entry = ttk.Entry(input_frame); moment_entry.pack()

ttk.Label(input_frame, text="Design code:").pack()
code_var = tk.StringVar(value='EUROCODE')
ttk.Combobox(input_frame, textvariable=code_var, values=['EUROCODE', 'ACI']).pack()

ttk.Button(input_frame, text="Run Analysis", command=run_analysis).pack(pady=5)
ttk.Button(input_frame, text="Export Summary + Diagram", command=export_results).pack(pady=5)

canvas = None
root.mainloop()