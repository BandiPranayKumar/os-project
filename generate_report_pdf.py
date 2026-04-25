from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


OUTPUT_PATH = r"C:\Users\pnikh\Documents\Codex\2026-04-18-files-mentioned-by-the-user-about\final_touch\ARAMS_Project_Report_Final.pdf"


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="TitleCenter",
        parent=styles["Title"],
        fontName="Times-Bold",
        fontSize=20,
        leading=24,
        alignment=TA_CENTER,
        spaceAfter=12,
    )
)
styles.add(
    ParagraphStyle(
        name="SubCenter",
        parent=styles["Normal"],
        fontName="Times-Roman",
        fontSize=12,
        leading=16,
        alignment=TA_CENTER,
        spaceAfter=10,
    )
)
styles.add(
    ParagraphStyle(
        name="HeadingMain",
        parent=styles["Heading1"],
        fontName="Times-Bold",
        fontSize=16,
        leading=20,
        spaceBefore=10,
        spaceAfter=10,
    )
)
styles.add(
    ParagraphStyle(
        name="HeadingSub",
        parent=styles["Heading2"],
        fontName="Times-Bold",
        fontSize=13,
        leading=17,
        spaceBefore=8,
        spaceAfter=8,
    )
)
styles.add(
    ParagraphStyle(
        name="BodyTextCustom",
        parent=styles["BodyText"],
        fontName="Times-Roman",
        fontSize=11,
        leading=17,
        alignment=TA_JUSTIFY,
        spaceAfter=8,
    )
)
styles.add(
    ParagraphStyle(
        name="BulletCustom",
        parent=styles["BodyText"],
        fontName="Times-Roman",
        fontSize=11,
        leading=16,
        leftIndent=18,
        firstLineIndent=-10,
        spaceAfter=5,
    )
)


def p(text, style="BodyTextCustom"):
    return Paragraph(text, styles[style])


story = []

story.extend(
    [
        Spacer(1, 1.0 * inch),
        Paragraph("PROJECT REPORT", styles["TitleCenter"]),
        Paragraph("on", styles["SubCenter"]),
        Paragraph("Adaptive Resource Allocation in Multiprogramming Systems", styles["TitleCenter"]),
        Spacer(1, 0.25 * inch),
        Paragraph("Submitted in partial fulfillment of academic project/report requirements", styles["SubCenter"]),
        Spacer(1, 0.55 * inch),
        Paragraph("Prepared For", styles["SubCenter"]),
        Paragraph("Lovely Professional University", styles["SubCenter"]),
        Paragraph("School of Computer Science and Engineering", styles["SubCenter"]),
        Spacer(1, 0.55 * inch),
        Paragraph("Prepared By", styles["SubCenter"]),
        Paragraph("[Student Name]", styles["SubCenter"]),
        Paragraph("[Registration Number]", styles["SubCenter"]),
        Spacer(1, 0.55 * inch),
        Paragraph("Guide / Mentor", styles["SubCenter"]),
        Paragraph("[Faculty Name]", styles["SubCenter"]),
        Spacer(1, 1.0 * inch),
        Paragraph("Session: 2026", styles["SubCenter"]),
        PageBreak(),
    ]
)

story.append(Paragraph("Certificate / Declaration", styles["HeadingMain"]))
story.append(
    p(
        "This is to certify that the project report entitled <b>Adaptive Resource Allocation in Multiprogramming "
        "Systems</b> is a record of project work prepared for academic evaluation. The report describes the design, "
        "implementation, simulation workflow, and demonstration website created to explain how CPU and memory can be "
        "monitored and dynamically adjusted among multiple programs in order to improve overall system utilization. "
        "All placeholders such as student name, registration number, and guide name may be filled as per submission requirements."
    )
)
story.append(Spacer(1, 0.25 * inch))
story.append(p("Student Signature: ____________________", "BodyTextCustom"))
story.append(p("Guide Signature: ____________________", "BodyTextCustom"))
story.append(p("Date: ____________________", "BodyTextCustom"))
story.append(PageBreak())

story.append(Paragraph("Abstract", styles["HeadingMain"]))
story.append(
    p(
        "Multiprogramming systems execute several programs concurrently, which creates competition for limited hardware "
        "resources such as CPU time and memory. A static allocation policy often fails to handle dynamic workload variations. "
        "As a result, some processes may experience starvation, long waiting time, or inefficient execution while others occupy "
        "more resources than required. The objective of this project is to demonstrate the concept of adaptive resource allocation "
        "through a live, interactive, web-based simulation."
    )
)
story.append(
    p(
        "The implemented system simulates continuous monitoring of CPU usage, memory usage, process priority, throughput, "
        "latency, and adaptation count. Based on changing conditions, the system updates process behavior and shows how resources "
        "can be redistributed in different operating modes such as normal load, stress load, and priority shift. The professional "
        "version of the project also includes an optional AI-assisted recommendation block that can interpret the current metrics "
        "and suggest corrective actions."
    )
)
story.append(
    p(
        "The project is implemented using HTML, CSS, JavaScript, Node.js, Express.js, Socket.IO, and Chart.js. The result is a "
        "dashboard-oriented website that converts an operating systems concept into a practical visual demonstration. The system does "
        "not replace a real operating system scheduler, but it effectively explains the logic of adaptive resource management and "
        "serves as a useful academic prototype for presentation and discussion."
    )
)
story.append(PageBreak())

story.append(Paragraph("Acknowledgement", styles["HeadingMain"]))
story.append(
    p(
        "I would like to express sincere gratitude to my faculty mentor, department, and Lovely Professional University for "
        "providing the academic environment required to complete this project work. I also acknowledge the use of development "
        "tools, web documentation, and guided assistance in understanding implementation details related to Node.js, Socket.IO, "
        "frontend design, and simulated dashboard behavior."
    )
)

story.append(Paragraph("Table of Contents", styles["HeadingMain"]))
toc_items = [
    "1. Project Overview",
    "2. Module-Wise Breakdown",
    "3. Functionalities",
    "4. Technology Used",
    "5. Flow Diagram and Workflow Explanation",
    "6. Revision Tracking on GitHub",
    "7. Conclusion and Future Scope",
    "8. References",
    "Appendix A. AI-Generated Project Elaboration / Breakdown Report",
    "Appendix B. Problem Statement",
    "Appendix C. Solution / Code Inventory",
]
for item in toc_items:
    story.append(p(item, "BulletCustom"))
story.append(PageBreak())

story.append(Paragraph("1. Project Overview", styles["HeadingMain"]))
overview_paragraphs = [
    "Adaptive Resource Allocation in Multiprogramming Systems is a concept-driven academic project intended to show how a computer system can distribute limited resources such as CPU time and memory among multiple running programs in a more intelligent and flexible manner. In a basic multiprogramming system, more than one process exists in memory and the processor switches among them. When the number of active processes increases, the system may encounter contention, resource imbalance, delayed execution, and reduced throughput. This project attempts to explain how such problems can be reduced when allocation decisions are based on current load conditions instead of fixed rules.",
    "The project has been implemented as a web-based demonstration platform so that the underlying idea can be explained visually. Instead of only writing theoretical concepts, the project presents the idea through a multi-page website containing a landing page, feature page, architecture page, about page, contact page, and most importantly a live demo page. The demo page simulates CPU pressure, memory pressure, process conditions, efficiency, throughput, and latency. It then updates graphs, bars, and tables in real time so that a viewer can observe how the system responds under different simulated conditions.",
    "The final professional version of the project emphasizes both academic explanation and presentation quality. The site has a polished interface, responsive layout, real-time dashboard components, and structured navigation. While the backend does not control actual operating system level resources, it simulates realistic resource behavior in a way that helps a student explain adaptive scheduling, monitoring, and reallocation decisions during a class presentation, viva, or project review.",
    "The project primarily demonstrates three ideas. First, the system should continuously monitor important performance indicators. Second, the system should detect when load changes create an imbalance or bottleneck. Third, the system should react by adjusting the share of resources or changing the priority of certain workloads. These three ideas form the conceptual foundation of adaptive resource allocation and are visible throughout the site design, live demo, and system architecture explanation.",
]
for text in overview_paragraphs:
    story.append(p(text))

story.append(Paragraph("Project Objectives", styles["HeadingSub"]))
for bullet in [
    "To simulate a system that monitors CPU and memory usage continuously.",
    "To demonstrate how load changes can affect process performance in a multiprogramming environment.",
    "To visualize how dynamic reallocation can improve responsiveness and reduce bottlenecks.",
    "To build a presentable, interactive dashboard for academic explanation.",
    "To provide a structured web-based report of the concept using multiple modules.",
]:
    story.append(p(f"• {bullet}", "BulletCustom"))

story.append(PageBreak())

story.append(Paragraph("2. Module-Wise Breakdown", styles["HeadingMain"]))
modules = {
    "2.1 Home Module": "The home module acts as the introductory interface of the project. It presents the title of the system, describes the project in concise academic language, and provides a first visual impression of what the dashboard represents. It contains a summary of the project purpose, quick metrics, and a visual resource snapshot. The main function of this module is to ensure that any viewer immediately understands that the project is related to dynamic CPU and memory optimization in a multiprogramming environment.",
    "2.2 Features Module": "The features module lists the major capabilities and conceptual strengths of the project. These include real-time monitoring, predictive insight, dynamic reallocation, and improved system stability. It converts the technical idea into structured points that can be used during presentation. This module is important because it connects the problem statement with the practical outputs of the system.",
    "2.3 System Architecture Module": "The system module explains the internal workflow of the project using a stage-based structure. In the professional version, the architecture is described with Observe, Analyze, and Act phases. This gives a simplified but meaningful explanation of how resource allocation systems operate. Metrics are first observed, then interpreted, and then used to influence scheduling or allocation choices.",
    "2.4 Live Demo Module": "The live demo module is the central part of the project. It presents a running simulation of CPU usage, memory usage, efficiency, throughput, adaptation count, and individual process states. It also allows the user to switch among different workload modes such as normal load, stress test, and priority shift. This module transforms theory into behavior by showing how the system changes when the environment changes.",
    "2.5 AI Allocation Advisor Module": "In the professional version, the AI allocation advisor is an optional enhancement that accepts an OpenAI API key and sends the current system metrics to the backend. The backend then requests a compact recommendation from the model and returns a structured response containing summary, primary risk, recommended action, and expected impact. This module extends the project from simulation to interpretation and demonstrates how AI can support system monitoring decisions.",
    "2.6 About Module": "The about module provides project background, domain context, and the educational purpose of the system. It is designed to help evaluators understand why the project was built and how it relates to operating systems. It also supports project storytelling by summarizing the problem domain in a readable form.",
    "2.7 Contact Module": "The contact module contains a form and context information. Although it is not part of the operating systems logic, it completes the site as a professional web project. It demonstrates form handling, page consistency, and frontend interaction, all of which contribute to the overall usability of the system showcase.",
    "2.8 Backend Server Module": "The backend server module is built with Node.js and Express.js. It serves the website files, provides API endpoints, and simulates changing system data over time. This module is responsible for generating workload metrics, exposing them to the frontend, and coordinating real-time updates through Socket.IO.",
    "2.9 Real-Time Communication Module": "The communication module uses Socket.IO to push changing system data from the server to the browser. This allows the demo page to update without requiring manual refresh. It is a key part of the live dashboard because it creates the impression of a continuously monitored system.",
}
for title, text in modules.items():
    story.append(Paragraph(title, styles["HeadingSub"]))
    story.append(p(text))

story.append(PageBreak())

story.append(Paragraph("3. Functionalities", styles["HeadingMain"]))
for bullet in [
    "Multi-page website with professional navigation structure.",
    "Live simulation of CPU usage and memory utilization.",
    "Real-time updates of process-level information such as ID, service name, CPU share, memory usage, priority, and status.",
    "Performance trend chart visualizing CPU and memory behavior over recent time intervals.",
    "Mode switching between normal load, stress test, and priority shift.",
    "Calculation and display of throughput, latency, efficiency, and total adaptations.",
    "Interactive contact form for presentation completeness.",
    "Responsive design for desktop and mobile viewing.",
    "Optional AI-generated insight based on current system metrics.",
]:
    story.append(p(f"• {bullet}", "BulletCustom"))

story.append(Paragraph("Functional Understanding", styles["HeadingSub"]))
for text in [
    "The project does not directly change hardware resource allocation in the operating system. Instead, it simulates the logic of an adaptive allocation system in a clear and interactive form.",
    "Whenever the workload mode changes, the backend updates CPU and memory baselines, latency values, throughput values, efficiency values, and process status information. This lets the viewer observe how a scheduler or allocator might behave under changed conditions.",
    "The professional version also interprets these live metrics through an optional AI recommendation block. This demonstrates how system telemetry can be paired with modern analysis tools to produce human-readable optimization suggestions.",
]:
    story.append(p(text))

story.append(PageBreak())

story.append(Paragraph("4. Technology Used", styles["HeadingMain"]))

tech_data = [
    ["Category", "Technology", "Purpose"],
    ["Programming Languages", "HTML, CSS, JavaScript", "Frontend structure, styling, and interaction"],
    ["Runtime", "Node.js", "Backend execution environment"],
    ["Framework", "Express.js", "Routing and server-side APIs"],
    ["Realtime Library", "Socket.IO", "Live system updates from server to client"],
    ["Charting", "Chart.js", "Performance trend visualization"],
    ["Styling Assets", "Google Fonts, Font Awesome", "Typography and icons"],
    ["Package Manager", "npm", "Dependency management"],
    ["Development Tool", "VS Code", "Code editing and testing"],
    ["Version Control", "Git / GitHub", "Revision tracking and repository hosting"],
]

table = Table(tech_data, colWidths=[1.5 * inch, 1.8 * inch, 3.0 * inch])
table.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#d9e3f0")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"),
            ("FONTNAME", (0, 1), (-1, -1), "Times-Roman"),
            ("FONTSIZE", (0, 0), (-1, -1), 10),
            ("LEADING", (0, 0), (-1, -1), 13),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f7f9fc")]),
        ]
    )
)
story.append(table)
story.append(Spacer(1, 0.15 * inch))
story.append(
    p(
        "According to general LPU-style report guidelines available in student-shared formatting documents, A4 paper, "
        "Times New Roman, and a structured chapter-oriented layout are commonly expected. This report follows that general spirit "
        "while keeping the content aligned with the actual project implementation."
    )
)

story.append(PageBreak())

story.append(Paragraph("5. Flow Diagram and Workflow Explanation", styles["HeadingMain"]))
for text in [
    "The conceptual workflow of the project can be explained as a loop. The server begins by creating baseline system metrics. These metrics include CPU usage, memory usage, process-level details, throughput, and efficiency. The current operating mode determines the broad resource condition. For example, stress mode increases usage and latency, while priority mode boosts selected processes.",
    "Next, the backend updates process states and emits the new values through Socket.IO. The browser listens for these updates and redraws the bars, labels, process table, and performance chart. If the AI advisor is used, the current metrics are also converted into a prompt and sent to the OpenAI API for structured interpretation.",
]:
    story.append(p(text))

flow_steps = [
    "Start system and initialize baseline metrics",
    "Collect or simulate CPU, memory, and process data",
    "Identify current workload mode",
    "Apply mode-specific profile and update resource values",
    "Emit new metrics to the frontend using Socket.IO",
    "Render charts, progress bars, and process table",
    "Optionally generate AI recommendation from current metrics",
    "Repeat cycle to simulate continuous monitoring",
]
for index, step in enumerate(flow_steps, start=1):
    story.append(p(f"{index}. {step}", "BulletCustom"))

story.append(Paragraph("Textual Flow Diagram", styles["HeadingSub"]))
for line in [
    "User opens demo page",
    "→ Frontend connects to server",
    "→ Server emits live system state",
    "→ Dashboard updates CPU / Memory / Efficiency panels",
    "→ Chart and process table refresh",
    "→ User changes mode if needed",
    "→ Server recalculates state",
    "→ Optional AI insight analyzes current metrics",
]:
    story.append(p(line, "BulletCustom"))

story.append(PageBreak())

story.append(Paragraph("6. Revision Tracking on GitHub", styles["HeadingMain"]))
story.append(p("Repository Name: [Insert Repository Name]"))
story.append(p("GitHub Link: [Insert Repository URL]"))
story.append(
    p(
        "The project can be version controlled using Git and hosted on GitHub. Revision tracking is important because it records "
        "every major change made to the interface, backend logic, simulation behavior, and report content. For academic submission, "
        "GitHub can serve as evidence of iterative development. It can also be used to show the difference between early design drafts, "
        "student-friendly versions, and the final presentation-oriented version."
    )
)
story.append(
    p(
        "Suggested commit categories for this project include: initial project setup, multi-page layout creation, backend simulation module, "
        "Socket.IO integration, dashboard chart integration, UI polish, demo fixes, and report generation. If the repository has not been "
        "created yet, this section may be completed later before final submission."
    )
)

story.append(Paragraph("7. Conclusion and Future Scope", styles["HeadingMain"]))
story.append(
    p(
        "This project successfully demonstrates the idea of adaptive resource allocation in a way that is both technically meaningful and "
        "easy to present. By combining a real-time simulation backend with a dashboard-based frontend, the project communicates how a system "
        "could monitor load, detect imbalance, and respond by changing allocation behavior. The professional version improves the quality of "
        "presentation and gives the project a complete and polished identity."
    )
)
story.append(
    p(
        "Future improvements can make the project more advanced and closer to a real system. Instead of simulated values, real operating system "
        "metrics can be collected through system-level tools or libraries. A machine learning model can be trained on historical usage data to "
        "predict future spikes more accurately. The project may also be extended to include disk I/O, network utilization, thread-level metrics, "
        "and persistence of historical dashboard data in a database. Finally, the system can be deployed online and provided with user authentication "
        "for a more complete software engineering experience."
    )
)
for bullet in [
    "Use actual system metrics instead of simulated metrics",
    "Add database support for logging and history analysis",
    "Integrate advanced scheduling algorithms",
    "Support disk and network resource monitoring",
    "Deploy the dashboard to cloud hosting",
    "Improve security, API key handling, and access control",
]:
    story.append(p(f"• {bullet}", "BulletCustom"))

story.append(PageBreak())

story.append(Paragraph("8. References", styles["HeadingMain"]))
references = [
    "Node.js Documentation. Available at: https://nodejs.org/",
    "Express.js Documentation. Available at: https://expressjs.com/",
    "Socket.IO Documentation. Available at: https://socket.io/docs/",
    "Chart.js Documentation. Available at: https://www.chartjs.org/docs/",
    "MDN Web Docs. Available at: https://developer.mozilla.org/",
    "Google Fonts Documentation. Available at: https://fonts.google.com/",
    "Font Awesome Documentation. Available at: https://fontawesome.com/",
    "Student-shared LPU report formatting references discussing A4 paper, Times New Roman, margins, and structured content order (examples from Studocu/CourseHero style mirrored materials).",
]
for ref in references:
    story.append(p(f"• {ref}", "BulletCustom"))

story.append(PageBreak())

story.append(Paragraph("Appendix A. AI-Generated Project Elaboration / Breakdown Report", styles["HeadingMain"]))
appendix_a = [
    "This project is based on the concept of adaptive resource allocation in multiprogramming systems. In such systems, multiple processes run together and compete for shared hardware resources. If the allocation policy is static, one process may consume more CPU or memory than needed while others wait for service. This leads to increased latency, lower throughput, and poor utilization.",
    "To explain the solution, the project uses a simulation-driven dashboard approach. The backend generates continuously changing system values. These values reflect different states of load and process demand. The frontend then displays them through an interactive dashboard containing bars, charts, and process tables. This allows a user to understand how resource pressure changes over time and how the system can react dynamically.",
    "The live demo is the strongest part of the project because it converts an abstract operating systems concept into something visible and explainable. When the viewer changes the system mode from normal to stress, the effects become immediately visible. CPU and memory rise, latency changes, and process states fluctuate. This demonstrates the need for intelligent control in systems where many programs execute together.",
    "The AI advisor in the professional version adds an optional interpretation layer. Instead of only showing numbers, it produces short recommendations such as identifying the main risk or suggesting a priority change. This shows how modern monitoring systems can be enhanced with AI-powered insight, even though the base project remains focused on adaptive resource allocation.",
]
for text in appendix_a:
    story.append(p(text))

story.append(Paragraph("Appendix B. Problem Statement", styles["HeadingMain"]))
story.append(
    p(
        "Develop a system that dynamically adjusts resource allocation among multiple programs to optimize CPU and memory utilization. "
        "The solution should monitor system performance and reallocate resources in real time to prevent bottlenecks."
    )
)

story.append(Paragraph("Appendix C. Solution / Code Inventory", styles["HeadingMain"]))
story.append(
    p(
        "The full codebase for the professional version is maintained in the project folder and should be attached with the submission. "
        "For report readability, the complete code is referenced here by file inventory instead of printing every line directly inside the report body."
    )
)
for item in [
    "server.js - backend server, API routes, live simulation logic, Socket.IO updates, OpenAI insight route",
    "package.json - project metadata, scripts, and dependencies",
    "public/index.html - home page",
    "public/features.html - features page",
    "public/system.html - architecture page",
    "public/demo.html - live dashboard and AI insight interface",
    "public/about.html - project context page",
    "public/contact.html - contact form page",
    "public/style.css - design system, layout, cards, dashboard visuals",
    "public/script.js - frontend behavior, chart rendering, realtime updates, AI request logic",
]:
    story.append(p(f"• {item}", "BulletCustom"))

story.append(
    p(
        "If the faculty specifically requires complete source code in the printed appendix, the above files may be copied after this section as Annexure pages. "
        "However, due to size constraints, many project reports attach code separately in digital form while summarizing file responsibilities in the main report."
    )
)


def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont("Times-Roman", 10)
    canvas.drawRightString(A4[0] - 50, 20, f"Page {doc.page}")
    canvas.restoreState()


doc = SimpleDocTemplate(
    OUTPUT_PATH,
    pagesize=A4,
    rightMargin=0.9 * inch,
    leftMargin=1.1 * inch,
    topMargin=0.9 * inch,
    bottomMargin=0.8 * inch,
)
doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
print(OUTPUT_PATH)
