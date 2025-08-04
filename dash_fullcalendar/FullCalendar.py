# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[typing.Union[str, int, float, Component, None]],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


class FullCalendar(Component):
    """A FullCalendar component.
DashFullCalendar – thin Dash wrapper around @fullcalendar/react.
ALL props (except the Dash house‑keeping ones) are forwarded verbatim.
No monkey‑patching of FullCalendar internals.

Keyword arguments:

- id (string; optional):
    Unique HTML id for the calendar container.  See FullCalendar docs.

- allDayClassNames (list | dict | string; optional):
    Class names for the all-day row.  See FullCalendar docs.

- allDayContent (a list of or a singular dash component, string or number; optional):
    Custom renderer for the all-day cell.  See FullCalendar docs.

- allDaySlot (boolean; optional):
    Display the all-day row in time-grid views.  See FullCalendar
    docs.

- allDayText (string; optional):
    Text label for the all-day slot.  See FullCalendar docs.

- aspectRatio (number; optional):
    Width/height ratio when `height` is auto.  See FullCalendar docs.

- businessHours (boolean | dict | list; optional):
    Business-hours definition(s) or `True` for default.  See
    FullCalendar docs.

- buttonIcons (dict; optional):
    Icon class strings mapped to built-in button names.  See
    FullCalendar docs.

- buttonText (dict; optional):
    Override text labels for built-in buttons.  See FullCalendar docs.

- command (dict; optional):
    An object specifying a command to execute on the calendar API,
    such as {'type': 'next'} to navigate to the next period.

- contentHeight (number | string; optional):
    Height of the scrollable content area.  See FullCalendar docs.

- customButtons (dict; optional):
    Custom button definitions keyed by name.  See FullCalendar docs.

- dateClick (boolean | number | string | dict | list; optional):
    The date string of the clicked date, for use in Dash callbacks.

- datesSet (boolean | number | string | dict | list; optional):
    Object containing the current date range, for use in Dash
    callbacks.

- dayCellClassNames (list | dict | string; optional):
    Class names for day cells.  See FullCalendar docs.

- dayCellContent (a list of or a singular dash component, string or number; optional):
    Custom renderer for day cells.  See FullCalendar docs.

- dayHeaderClassNames (list | dict | string; optional):
    Class names for day headers.  See FullCalendar docs.

- dayHeaderContent (a list of or a singular dash component, string or number; optional):
    Custom renderer for day headers.  See FullCalendar docs.

- dayHeaderFormat (dict | string; optional):
    Formatter for day-header text.  See FullCalendar docs.

- dayMaxEventRows (boolean | number; optional):
    Alternate way to cap events per day (rows).  See FullCalendar
    docs.

- dayMaxEvents (boolean | number; optional):
    Collapse rows after this many events per day.  See FullCalendar
    docs.

- dayMinWidth (number; optional):
    Minimum pixel width of a day column.  See FullCalendar docs.

- dayPopoverFormat (dict | string; optional):
    Date-format skeleton for the day popover.  See FullCalendar docs.

- defaultAllDay (boolean; optional):
    Default all-day status for new events.  See FullCalendar docs.

- dir (string; optional):
    Text direction: ‘ltr’ or ‘rtl’.  See FullCalendar docs.

- displayEventEnd (boolean; optional):
    Show event end time.  See FullCalendar docs.

- displayEventTime (boolean; optional):
    Show event time.  See FullCalendar docs.

- dragRevertDuration (number; optional):
    Duration for drag revert animation.  See FullCalendar docs.

- dragScroll (boolean; optional):
    Allow calendar to scroll during drag.  See FullCalendar docs.

- dropAccept (string; optional):
    Selector or function to accept drops.  See FullCalendar docs.

- droppable (boolean; optional):
    Allow external elements to be dropped.  See FullCalendar docs.

- editable (boolean; optional):
    Allow events to be editable.  See FullCalendar docs.

- endParam (string; optional):
    Name of end date GET param.  See FullCalendar docs.

- eventAdd (boolean | number | string | dict | list; optional):
    Object containing information about the added event, for use in
    Dash callbacks.

- eventBackgroundColor (string; optional):
    Default background color for events.  See FullCalendar docs.

- eventBorderColor (string; optional):
    Default border color for events.  See FullCalendar docs.

- eventChange (boolean | number | string | dict | list; optional):
    Object containing information about the changed event, for use in
    Dash callbacks.

- eventClassNames (list | dict | string; optional):
    Class names for events.  See FullCalendar docs.

- eventClick (boolean | number | string | dict | list; optional):
    Object containing information about the clicked event, for use in
    Dash callbacks.

- eventColor (string; optional):
    Default color for events.  See FullCalendar docs.

- eventConstraint (dict | string; optional):
    Event constraint for dragging/resizing.  See FullCalendar docs.

- eventContent (a list of or a singular dash component, string or number; optional):
    Custom renderer for events.  See FullCalendar docs.

- eventDisplay (string; optional):
    Rendering style for events.  See FullCalendar docs.

- eventDrop (boolean | number | string | dict | list; optional):
    Object containing information about the dropped event, for use in
    Dash callbacks.

- eventDurationEditable (boolean; optional):
    Allow event duration to be editable.  See FullCalendar docs.

- eventLongPressDelay (number; optional):
    Delay for event long press (ms).  See FullCalendar docs.

- eventOrder (list | string; optional):
    Determines event sort order.  See FullCalendar docs.

- eventOrderStrict (boolean; optional):
    Enforce strict event ordering.  See FullCalendar docs.

- eventOverlap (boolean; optional):
    Allow events to overlap.  See FullCalendar docs.

- eventRemove (boolean | number | string | dict | list; optional):
    Object containing information about the removed event, for use in
    Dash callbacks.

- eventResizableFromStart (boolean; optional):
    Allow resizing events from start.  See FullCalendar docs.

- eventResize (boolean | number | string | dict | list; optional):
    Object containing information about the resized event, for use in
    Dash callbacks.

- eventSources (list; optional):
    Array of event source objects.  See FullCalendar docs.

- eventStartEditable (boolean; optional):
    Allow event start to be editable.  See FullCalendar docs.

- eventTextColor (string; optional):
    Default text color for events.  See FullCalendar docs.

- eventTimeFormat (dict | string; optional):
    Formatter for event time text.  See FullCalendar docs.

- events (list | string; optional):
    Array, URL, or function that supplies the initial events.  See
    FullCalendar docs.

- eventsSet (boolean | number | string | dict | list; optional):
    Array of current event objects in the calendar, for use in Dash
    callbacks.

- expandRows (boolean; optional):
    When `True`, rows stretch to fill vertical space.  See
    FullCalendar docs.

- firstDay (number; optional):
    Index of week’s first day (0 = Sunday).  See FullCalendar docs.

- fixedWeekCount (boolean; optional):
    Always render 6 weeks in month view.  See FullCalendar docs.

- footerToolbar (dict | boolean; optional):
    Config for the bottom toolbar; set `False` to hide.  See
    FullCalendar docs.

- handleWindowResize (boolean; optional):
    Recompute dimensions on window resize.  See FullCalendar docs.

- headerToolbar (dict | boolean; optional):
    Config for the top toolbar; set `False` to hide.  See FullCalendar
    docs.

- height (number | string; optional):
    Overall calendar height (`number`, ‘auto’, ‘parent’, or function).
    See FullCalendar docs.

- hiddenDays (list; optional):
    Array of day numbers to hide (0 = Sun).  See FullCalendar docs.

- initialDate (string; optional):
    Date the calendar navigates to on first render.  See FullCalendar
    docs.

- initialView (string; optional):
    Name of the view the calendar shows on first load.  See
    FullCalendar docs.

- lazyFetching (boolean; optional):
    Fetch events only when needed.  See FullCalendar docs.

- listDayFormat (dict | string | boolean; optional):
    Formatter for list view group headers.  See FullCalendar docs.

- listDaySideFormat (dict | string | boolean; optional):
    Formatter for list view side headers.  See FullCalendar docs.

- locale (string; optional):
    Calendar locale code (e.g. ‘en-gb’).  See FullCalendar docs.

- locales (list; optional):
    Array of additional locale objects to load.  See FullCalendar
    docs.

- longPressDelay (number; optional):
    Delay for long press (ms).  See FullCalendar docs.

- moreLinkClassNames (list | dict | string; optional):
    Class names for the ‘+ more’ link.  See FullCalendar docs.

- moreLinkClick (string; optional):
    Action when a ‘+ more’ link is clicked.  See FullCalendar docs.

- moreLinkContent (a list of or a singular dash component, string or number; optional):
    Custom renderer for the ‘+ more’ link.  See FullCalendar docs.

- moreLinkText (string; optional):
    Text factory for the ‘+ more’ link.  See FullCalendar docs.

- multiMonthMaxColumns (number; optional):
    Max columns in multi-month view.  See FullCalendar docs.

- multiMonthMinWidth (number; optional):
    Min width for multi-month columns.  See FullCalendar docs.

- multiMonthTitleFormat (dict | string; optional):
    Title format for multi-month view.  See FullCalendar docs.

- navLinkDayClick (string; optional):
    Handler for day navigation link clicks.  See FullCalendar docs.

- navLinkHint (string; optional):
    Tooltip for navigation links.  See FullCalendar docs.

- navLinkWeekClick (string; optional):
    Handler for week navigation link clicks.  See FullCalendar docs.

- navLinks (boolean; optional):
    Enable day/week navigation links.  See FullCalendar docs.

- nextDayThreshold (string | dict; optional):
    Threshold for \"next day\" calculation.  See FullCalendar docs.

- noEventsClassNames (list | dict | string; optional):
    Class names applied when no events are present.  See FullCalendar
    docs.

- noEventsContent (a list of or a singular dash component, string or number; optional):
    Custom ‘no events’ content renderer.  See FullCalendar docs.

- now (string; optional):
    Function/string/Date returning the ‘current’ date.  See
    FullCalendar docs.

- nowIndicator (boolean; optional):
    Render a line marking the current time.  See FullCalendar docs.

- progressiveEventRendering (boolean; optional):
    Render events as they load.  See FullCalendar docs.

- rerenderDelay (number; optional):
    Delay before rerendering events.  See FullCalendar docs.

- scrollTime (string | dict; optional):
    Initial scroll position of time-grid views.  See FullCalendar
    docs.

- scrollTimeReset (boolean; optional):
    Reset scroll position when changing views.  See FullCalendar docs.

- select (boolean | number | string | dict | list; optional):
    Object containing the selected range information, for use in Dash
    callbacks.

- selectConstraint (dict | string; optional):
    Selection constraint for selecting.  See FullCalendar docs.

- selectLongPressDelay (number; optional):
    Delay for select long press (ms).  See FullCalendar docs.

- selectMinDistance (number; optional):
    Minimum drag distance before selection.  See FullCalendar docs.

- selectMirror (boolean; optional):
    Show a mirror of selection while dragging.  See FullCalendar docs.

- selectOverlap (boolean; optional):
    Allow selection to overlap events.  See FullCalendar docs.

- selectable (boolean; optional):
    Allow date/time range selection.  See FullCalendar docs.

- showNonCurrentDates (boolean; optional):
    Render leading/trailing days in month view.  See FullCalendar
    docs.

- slotDuration (string | dict; optional):
    Granularity of the vertical time slots.  See FullCalendar docs.

- slotLabelClassNames (list | dict | string; optional):
    Class names for slot labels.  See FullCalendar docs.

- slotLabelContent (a list of or a singular dash component, string or number; optional):
    Custom renderer for slot labels.  See FullCalendar docs.

- slotLabelFormat (list | dict | string; optional):
    Formatter(s) for slot labels.  See FullCalendar docs.

- slotLabelInterval (string | dict; optional):
    Interval between slot labels.  See FullCalendar docs.

- slotLaneClassNames (list | dict | string; optional):
    Class names for resource lanes.  See FullCalendar docs.

- slotLaneContent (a list of or a singular dash component, string or number; optional):
    Custom renderer for resource lanes.  See FullCalendar docs.

- slotMaxTime (string | dict; optional):
    Latest time shown on a day.  See FullCalendar docs.

- slotMinTime (string | dict; optional):
    Earliest time shown on a day.  See FullCalendar docs.

- slotMinWidth (number; optional):
    Minimum pixel width of a resource column.  See FullCalendar docs.

- snapDuration (string | dict; optional):
    Grid snapping interval while dragging.  See FullCalendar docs.

- startParam (string; optional):
    Name of start date GET param.  See FullCalendar docs.

- stickyFooterScrollbar (boolean; optional):
    Show sticky scrollbar at the bottom.  See FullCalendar docs.

- stickyHeaderDates (boolean; optional):
    Keep date headers fixed while scrolling.  See FullCalendar docs.

- themeSystem (string; optional):
    Theme system to apply to built-in UI (e.g. ‘standard’,
    ‘bootstrap5’).  See FullCalendar docs.

- timeZoneParam (string; optional):
    Name of time zone GET param.  See FullCalendar docs.

- titleFormat (dict | string; optional):
    Date-formatting skeleton or object for the view title.  See
    FullCalendar docs.

- unselect (boolean | number | string | dict | list; optional):
    Flag indicating unselection occurred, for use in Dash callbacks.

- unselectAuto (boolean; optional):
    Unselect when clicking outside.  See FullCalendar docs.

- unselectCancel (string; optional):
    CSS selector for elements that prevent unselect.  See FullCalendar
    docs.

- validRange (dict; optional):
    Restricts navigation/selection to a date range.  See FullCalendar
    docs.

- viewClassNames (list | dict | string; optional):
    Class names for the view container.  See FullCalendar docs.

- views (dict; optional):
    Custom view definitions mapped by name.  See FullCalendar docs.

- weekNumberCalculation (string; optional):
    Custom week-number algorithm.  See FullCalendar docs.

- weekNumberFormat (dict | string; optional):
    Formatter for week-number text.  See FullCalendar docs.

- weekNumbers (boolean; optional):
    Show ISO week numbers down the side.  See FullCalendar docs.

- weekText (string; optional):
    Short label preceding week numbers.  See FullCalendar docs.

- weekTextLong (string; optional):
    Long label preceding week numbers.  See FullCalendar docs.

- weekends (boolean; optional):
    Show weekend columns.  See FullCalendar docs.

- windowResizeDelay (number; optional):
    Debounce (ms) for the resize handler.  See FullCalendar docs."""
    _children_props = ['moreLinkContent', 'allDayContent', 'slotLaneContent', 'slotLabelContent', 'dayHeaderContent', 'dayCellContent', 'noEventsContent', 'eventContent']
    _base_nodes = ['moreLinkContent', 'allDayContent', 'slotLaneContent', 'slotLabelContent', 'dayHeaderContent', 'dayCellContent', 'noEventsContent', 'eventContent', 'children']
    _namespace = 'dash_fullcalendar'
    _type = 'FullCalendar'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        initialView: typing.Optional[str] = None,
        events: typing.Optional[typing.Union[typing.Sequence, str, typing.Any]] = None,
        headerToolbar: typing.Optional[typing.Union[dict, bool]] = None,
        footerToolbar: typing.Optional[typing.Union[dict, bool]] = None,
        customButtons: typing.Optional[dict] = None,
        buttonIcons: typing.Optional[dict] = None,
        buttonText: typing.Optional[dict] = None,
        themeSystem: typing.Optional[str] = None,
        height: typing.Optional[typing.Union[NumberType, str, typing.Any]] = None,
        contentHeight: typing.Optional[typing.Union[NumberType, str, typing.Any]] = None,
        aspectRatio: typing.Optional[NumberType] = None,
        expandRows: typing.Optional[bool] = None,
        handleWindowResize: typing.Optional[bool] = None,
        windowResizeDelay: typing.Optional[NumberType] = None,
        stickyHeaderDates: typing.Optional[bool] = None,
        stickyFooterScrollbar: typing.Optional[bool] = None,
        initialDate: typing.Optional[typing.Union[str, typing.Any]] = None,
        validRange: typing.Optional[typing.Union[dict, typing.Any]] = None,
        visibleRange: typing.Optional[typing.Any] = None,
        titleFormat: typing.Optional[typing.Union[dict, str]] = None,
        locale: typing.Optional[str] = None,
        locales: typing.Optional[typing.Sequence] = None,
        dir: typing.Optional[str] = None,
        firstDay: typing.Optional[NumberType] = None,
        weekends: typing.Optional[bool] = None,
        hiddenDays: typing.Optional[typing.Sequence] = None,
        fixedWeekCount: typing.Optional[bool] = None,
        showNonCurrentDates: typing.Optional[bool] = None,
        dayMaxEvents: typing.Optional[typing.Union[bool, NumberType]] = None,
        dayMaxEventRows: typing.Optional[typing.Union[bool, NumberType]] = None,
        dayMinWidth: typing.Optional[NumberType] = None,
        moreLinkClick: typing.Optional[typing.Union[str, typing.Any]] = None,
        moreLinkContent: typing.Optional[typing.Union[typing.Any, ComponentType]] = None,
        moreLinkText: typing.Optional[typing.Union[str, typing.Any]] = None,
        moreLinkClassNames: typing.Optional[typing.Union[typing.Sequence, dict, str, typing.Any]] = None,
        moreLinkDidMount: typing.Optional[typing.Any] = None,
        moreLinkWillUnmount: typing.Optional[typing.Any] = None,
        dayPopoverFormat: typing.Optional[typing.Union[dict, str]] = None,
        weekNumbers: typing.Optional[bool] = None,
        weekNumberFormat: typing.Optional[typing.Union[dict, str]] = None,
        weekNumberCalculation: typing.Optional[typing.Union[str, typing.Any]] = None,
        weekText: typing.Optional[str] = None,
        weekTextLong: typing.Optional[str] = None,
        businessHours: typing.Optional[typing.Union[bool, dict, typing.Sequence]] = None,
        now: typing.Optional[typing.Union[str, typing.Any]] = None,
        nowIndicator: typing.Optional[bool] = None,
        scrollTime: typing.Optional[typing.Union[str, dict]] = None,
        scrollTimeReset: typing.Optional[bool] = None,
        slotDuration: typing.Optional[typing.Union[str, dict]] = None,
        slotLabelInterval: typing.Optional[typing.Union[str, dict]] = None,
        slotLabelFormat: typing.Optional[typing.Union[typing.Sequence, dict, str]] = None,
        slotMinTime: typing.Optional[typing.Union[str, dict]] = None,
        slotMaxTime: typing.Optional[typing.Union[str, dict]] = None,
        slotMinWidth: typing.Optional[NumberType] = None,
        snapDuration: typing.Optional[typing.Union[str, dict]] = None,
        allDaySlot: typing.Optional[bool] = None,
        allDayText: typing.Optional[str] = None,
        allDayClassNames: typing.Optional[typing.Union[typing.Sequence, dict, str, typing.Any]] = None,
        allDayContent: typing.Optional[typing.Union[typing.Any, ComponentType]] = None,
        allDayDidMount: typing.Optional[typing.Any] = None,
        allDayWillUnmount: typing.Optional[typing.Any] = None,
        slotLaneClassNames: typing.Optional[typing.Union[typing.Sequence, dict, str, typing.Any]] = None,
        slotLaneContent: typing.Optional[typing.Union[typing.Any, ComponentType]] = None,
        slotLaneDidMount: typing.Optional[typing.Any] = None,
        slotLaneWillUnmount: typing.Optional[typing.Any] = None,
        slotLabelClassNames: typing.Optional[typing.Union[typing.Sequence, dict, str, typing.Any]] = None,
        slotLabelContent: typing.Optional[typing.Union[typing.Any, ComponentType]] = None,
        slotLabelDidMount: typing.Optional[typing.Any] = None,
        slotLabelWillUnmount: typing.Optional[typing.Any] = None,
        dayHeaderFormat: typing.Optional[typing.Union[dict, str]] = None,
        dayHeaderClassNames: typing.Optional[typing.Union[typing.Sequence, dict, str, typing.Any]] = None,
        dayHeaderContent: typing.Optional[typing.Union[typing.Any, ComponentType]] = None,
        dayHeaderDidMount: typing.Optional[typing.Any] = None,
        dayHeaderWillUnmount: typing.Optional[typing.Any] = None,
        dayCellClassNames: typing.Optional[typing.Union[typing.Sequence, dict, str, typing.Any]] = None,
        dayCellContent: typing.Optional[typing.Union[typing.Any, ComponentType]] = None,
        dayCellDidMount: typing.Optional[typing.Any] = None,
        dayCellWillUnmount: typing.Optional[typing.Any] = None,
        listDayFormat: typing.Optional[typing.Union[dict, str, bool]] = None,
        listDaySideFormat: typing.Optional[typing.Union[dict, str, bool]] = None,
        noEventsClassNames: typing.Optional[typing.Union[typing.Sequence, dict, str, typing.Any]] = None,
        noEventsContent: typing.Optional[typing.Union[typing.Any, ComponentType]] = None,
        noEventsDidMount: typing.Optional[typing.Any] = None,
        noEventsWillUnmount: typing.Optional[typing.Any] = None,
        navLinks: typing.Optional[bool] = None,
        navLinkDayClick: typing.Optional[typing.Union[typing.Any, str]] = None,
        navLinkWeekClick: typing.Optional[typing.Union[typing.Any, str]] = None,
        navLinkHint: typing.Optional[typing.Union[str, typing.Any]] = None,
        multiMonthMaxColumns: typing.Optional[NumberType] = None,
        multiMonthMinWidth: typing.Optional[NumberType] = None,
        multiMonthTitleFormat: typing.Optional[typing.Union[dict, str]] = None,
        views: typing.Optional[dict] = None,
        eventSources: typing.Optional[typing.Sequence] = None,
        defaultAllDay: typing.Optional[bool] = None,
        eventTimeFormat: typing.Optional[typing.Union[dict, str]] = None,
        displayEventTime: typing.Optional[bool] = None,
        displayEventEnd: typing.Optional[bool] = None,
        nextDayThreshold: typing.Optional[typing.Union[str, dict]] = None,
        eventDisplay: typing.Optional[str] = None,
        eventBackgroundColor: typing.Optional[str] = None,
        eventBorderColor: typing.Optional[str] = None,
        eventTextColor: typing.Optional[str] = None,
        eventColor: typing.Optional[str] = None,
        eventOrder: typing.Optional[typing.Union[typing.Sequence, str, typing.Any]] = None,
        eventOrderStrict: typing.Optional[bool] = None,
        eventClassNames: typing.Optional[typing.Union[typing.Sequence, dict, str, typing.Any]] = None,
        eventContent: typing.Optional[typing.Union[typing.Any, ComponentType]] = None,
        eventDidMount: typing.Optional[typing.Any] = None,
        eventWillUnmount: typing.Optional[typing.Any] = None,
        eventDataTransform: typing.Optional[typing.Any] = None,
        startParam: typing.Optional[str] = None,
        endParam: typing.Optional[str] = None,
        timeZoneParam: typing.Optional[str] = None,
        lazyFetching: typing.Optional[bool] = None,
        progressiveEventRendering: typing.Optional[bool] = None,
        rerenderDelay: typing.Optional[NumberType] = None,
        loading: typing.Optional[typing.Any] = None,
        editable: typing.Optional[bool] = None,
        eventStartEditable: typing.Optional[bool] = None,
        eventResizableFromStart: typing.Optional[bool] = None,
        eventDurationEditable: typing.Optional[bool] = None,
        dragRevertDuration: typing.Optional[NumberType] = None,
        dragScroll: typing.Optional[bool] = None,
        droppable: typing.Optional[bool] = None,
        dropAccept: typing.Optional[typing.Union[str, typing.Any]] = None,
        eventOverlap: typing.Optional[typing.Union[bool, typing.Any]] = None,
        eventConstraint: typing.Optional[typing.Union[dict, str]] = None,
        eventAllow: typing.Optional[typing.Any] = None,
        selectable: typing.Optional[bool] = None,
        selectMirror: typing.Optional[bool] = None,
        unselectAuto: typing.Optional[bool] = None,
        unselectCancel: typing.Optional[str] = None,
        selectOverlap: typing.Optional[typing.Union[bool, typing.Any]] = None,
        selectConstraint: typing.Optional[typing.Union[dict, str]] = None,
        selectAllow: typing.Optional[typing.Any] = None,
        selectMinDistance: typing.Optional[NumberType] = None,
        longPressDelay: typing.Optional[NumberType] = None,
        eventLongPressDelay: typing.Optional[NumberType] = None,
        selectLongPressDelay: typing.Optional[NumberType] = None,
        viewClassNames: typing.Optional[typing.Union[typing.Sequence, dict, str, typing.Any]] = None,
        viewDidMount: typing.Optional[typing.Any] = None,
        viewWillUnmount: typing.Optional[typing.Any] = None,
        eventMouseEnter: typing.Optional[typing.Any] = None,
        eventMouseLeave: typing.Optional[typing.Any] = None,
        eventDragStart: typing.Optional[typing.Any] = None,
        eventDragStop: typing.Optional[typing.Any] = None,
        eventResizeStart: typing.Optional[typing.Any] = None,
        eventResizeStop: typing.Optional[typing.Any] = None,
        drop: typing.Optional[typing.Any] = None,
        eventReceive: typing.Optional[typing.Any] = None,
        eventLeave: typing.Optional[typing.Any] = None,
        command: typing.Optional[dict] = None,
        dateClick: typing.Optional[typing.Any] = None,
        select: typing.Optional[typing.Any] = None,
        unselect: typing.Optional[typing.Any] = None,
        eventClick: typing.Optional[typing.Any] = None,
        eventDrop: typing.Optional[typing.Any] = None,
        eventResize: typing.Optional[typing.Any] = None,
        eventAdd: typing.Optional[typing.Any] = None,
        eventChange: typing.Optional[typing.Any] = None,
        eventRemove: typing.Optional[typing.Any] = None,
        datesSet: typing.Optional[typing.Any] = None,
        eventsSet: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'allDayClassNames', 'allDayContent', 'allDaySlot', 'allDayText', 'aspectRatio', 'businessHours', 'buttonIcons', 'buttonText', 'command', 'contentHeight', 'customButtons', 'dateClick', 'datesSet', 'dayCellClassNames', 'dayCellContent', 'dayHeaderClassNames', 'dayHeaderContent', 'dayHeaderFormat', 'dayMaxEventRows', 'dayMaxEvents', 'dayMinWidth', 'dayPopoverFormat', 'defaultAllDay', 'dir', 'displayEventEnd', 'displayEventTime', 'dragRevertDuration', 'dragScroll', 'dropAccept', 'droppable', 'editable', 'endParam', 'eventAdd', 'eventBackgroundColor', 'eventBorderColor', 'eventChange', 'eventClassNames', 'eventClick', 'eventColor', 'eventConstraint', 'eventContent', 'eventDisplay', 'eventDrop', 'eventDurationEditable', 'eventLongPressDelay', 'eventOrder', 'eventOrderStrict', 'eventOverlap', 'eventRemove', 'eventResizableFromStart', 'eventResize', 'eventSources', 'eventStartEditable', 'eventTextColor', 'eventTimeFormat', 'events', 'eventsSet', 'expandRows', 'firstDay', 'fixedWeekCount', 'footerToolbar', 'handleWindowResize', 'headerToolbar', 'height', 'hiddenDays', 'initialDate', 'initialView', 'lazyFetching', 'listDayFormat', 'listDaySideFormat', 'locale', 'locales', 'longPressDelay', 'moreLinkClassNames', 'moreLinkClick', 'moreLinkContent', 'moreLinkText', 'multiMonthMaxColumns', 'multiMonthMinWidth', 'multiMonthTitleFormat', 'navLinkDayClick', 'navLinkHint', 'navLinkWeekClick', 'navLinks', 'nextDayThreshold', 'noEventsClassNames', 'noEventsContent', 'now', 'nowIndicator', 'progressiveEventRendering', 'rerenderDelay', 'scrollTime', 'scrollTimeReset', 'select', 'selectConstraint', 'selectLongPressDelay', 'selectMinDistance', 'selectMirror', 'selectOverlap', 'selectable', 'showNonCurrentDates', 'slotDuration', 'slotLabelClassNames', 'slotLabelContent', 'slotLabelFormat', 'slotLabelInterval', 'slotLaneClassNames', 'slotLaneContent', 'slotMaxTime', 'slotMinTime', 'slotMinWidth', 'snapDuration', 'startParam', 'stickyFooterScrollbar', 'stickyHeaderDates', 'themeSystem', 'timeZoneParam', 'titleFormat', 'unselect', 'unselectAuto', 'unselectCancel', 'validRange', 'viewClassNames', 'views', 'weekNumberCalculation', 'weekNumberFormat', 'weekNumbers', 'weekText', 'weekTextLong', 'weekends', 'windowResizeDelay']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'allDayClassNames', 'allDayContent', 'allDaySlot', 'allDayText', 'aspectRatio', 'businessHours', 'buttonIcons', 'buttonText', 'command', 'contentHeight', 'customButtons', 'dateClick', 'datesSet', 'dayCellClassNames', 'dayCellContent', 'dayHeaderClassNames', 'dayHeaderContent', 'dayHeaderFormat', 'dayMaxEventRows', 'dayMaxEvents', 'dayMinWidth', 'dayPopoverFormat', 'defaultAllDay', 'dir', 'displayEventEnd', 'displayEventTime', 'dragRevertDuration', 'dragScroll', 'dropAccept', 'droppable', 'editable', 'endParam', 'eventAdd', 'eventBackgroundColor', 'eventBorderColor', 'eventChange', 'eventClassNames', 'eventClick', 'eventColor', 'eventConstraint', 'eventContent', 'eventDisplay', 'eventDrop', 'eventDurationEditable', 'eventLongPressDelay', 'eventOrder', 'eventOrderStrict', 'eventOverlap', 'eventRemove', 'eventResizableFromStart', 'eventResize', 'eventSources', 'eventStartEditable', 'eventTextColor', 'eventTimeFormat', 'events', 'eventsSet', 'expandRows', 'firstDay', 'fixedWeekCount', 'footerToolbar', 'handleWindowResize', 'headerToolbar', 'height', 'hiddenDays', 'initialDate', 'initialView', 'lazyFetching', 'listDayFormat', 'listDaySideFormat', 'locale', 'locales', 'longPressDelay', 'moreLinkClassNames', 'moreLinkClick', 'moreLinkContent', 'moreLinkText', 'multiMonthMaxColumns', 'multiMonthMinWidth', 'multiMonthTitleFormat', 'navLinkDayClick', 'navLinkHint', 'navLinkWeekClick', 'navLinks', 'nextDayThreshold', 'noEventsClassNames', 'noEventsContent', 'now', 'nowIndicator', 'progressiveEventRendering', 'rerenderDelay', 'scrollTime', 'scrollTimeReset', 'select', 'selectConstraint', 'selectLongPressDelay', 'selectMinDistance', 'selectMirror', 'selectOverlap', 'selectable', 'showNonCurrentDates', 'slotDuration', 'slotLabelClassNames', 'slotLabelContent', 'slotLabelFormat', 'slotLabelInterval', 'slotLaneClassNames', 'slotLaneContent', 'slotMaxTime', 'slotMinTime', 'slotMinWidth', 'snapDuration', 'startParam', 'stickyFooterScrollbar', 'stickyHeaderDates', 'themeSystem', 'timeZoneParam', 'titleFormat', 'unselect', 'unselectAuto', 'unselectCancel', 'validRange', 'viewClassNames', 'views', 'weekNumberCalculation', 'weekNumberFormat', 'weekNumbers', 'weekText', 'weekTextLong', 'weekends', 'windowResizeDelay']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FullCalendar, self).__init__(**args)

setattr(FullCalendar, "__init__", _explicitize_args(FullCalendar.__init__))
