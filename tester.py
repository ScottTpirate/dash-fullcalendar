from dash import Dash, html, Input, Output
import dash_fullcalendar as dcal

app = Dash(__name__)

app.layout = html.Div(
    [
        dcal.FullCalendar(
            id="cal",
            initialView="dayGridMonth",
            editable=True,
            # FullCalendar props passed unchanged:
            headerToolbar={"left": "prev,next today", "center": "title",
                           "right": "dayGridMonth,timeGridWeek"},
            events=[
                {"title": "Audit", "date": "2025-08-01"},
                {"title": "Go‑Live", "date": "2025-08-10"},
            ],
        ),
        html.Div(id="clicked"),
    ]
)


@app.callback(Output("clicked", "children"), Input("cal", "dateClick"))
def show_click(date):
    return f"You clicked {date}" if date else "Click a date on the calendar."


if __name__ == "__main__":
    app.run(debug=True)