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

- id (string; optional)

- allDayClassNames (list | dict | string; optional)

- allDayContent (a list of or a singular dash component, string or number; optional)

- allDaySlot (boolean; optional)

- allDayText (string; optional)

- aspectRatio (number; optional)

- businessHours (boolean | dict | list; optional)

- buttonIcons (dict; optional)

- buttonText (dict; optional)

- command (dict; optional):
    An object specifying a command to execute on the calendar API,
    such as {'type': 'next'} to navigate to the next period.

- contentHeight (number | string; optional)

- customButtons (dict; optional)

- dateClick (boolean | number | string | dict | list; optional):
    The date string of the clicked date, for use in Dash callbacks.

- datesSet (boolean | number | string | dict | list; optional):
    Object containing the current date range, for use in Dash
    callbacks.

- dayCellClassNames (list | dict | string; optional)

- dayCellContent (a list of or a singular dash component, string or number; optional)

- dayHeaderClassNames (list | dict | string; optional)

- dayHeaderContent (a list of or a singular dash component, string or number; optional)

- dayHeaderFormat (dict | string; optional)

- dayMaxEventRows (boolean | number; optional)

- dayMaxEvents (boolean | number; optional)

- dayMinWidth (number; optional)

- dayPopoverFormat (dict | string; optional)

- defaultAllDay (boolean; optional)

- dir (string; optional)

- displayEventEnd (boolean; optional)

- displayEventTime (boolean; optional)

- dragRevertDuration (number; optional)

- dragScroll (boolean; optional)

- dropAccept (string; optional)

- droppable (boolean; optional)

- editable (boolean; optional)

- endParam (string; optional)

- eventAdd (boolean | number | string | dict | list; optional):
    Object containing information about the added event, for use in
    Dash callbacks.

- eventBackgroundColor (string; optional)

- eventBorderColor (string; optional)

- eventChange (boolean | number | string | dict | list; optional):
    Object containing information about the changed event, for use in
    Dash callbacks.

- eventClassNames (list | dict | string; optional)

- eventClick (boolean | number | string | dict | list; optional):
    Object containing information about the clicked event, for use in
    Dash callbacks.

- eventColor (string; optional)

- eventConstraint (dict | string; optional)

- eventContent (a list of or a singular dash component, string or number; optional)

- eventDisplay (string; optional)

- eventDrop (boolean | number | string | dict | list; optional):
    Object containing information about the dropped event, for use in
    Dash callbacks.

- eventDurationEditable (boolean; optional)

- eventLongPressDelay (number; optional)

- eventOrder (list | string; optional)

- eventOrderStrict (boolean; optional)

- eventOverlap (boolean; optional)

- eventRemove (boolean | number | string | dict | list; optional):
    Object containing information about the removed event, for use in
    Dash callbacks.

- eventResizableFromStart (boolean; optional)

- eventResize (boolean | number | string | dict | list; optional):
    Object containing information about the resized event, for use in
    Dash callbacks.

- eventSources (list; optional)

- eventStartEditable (boolean; optional)

- eventTextColor (string; optional)

- eventTimeFormat (dict | string; optional)

- events (list | string; optional)

- eventsSet (boolean | number | string | dict | list; optional):
    Array of current event objects in the calendar, for use in Dash
    callbacks.

- expandRows (boolean; optional)

- firstDay (number; optional)

- fixedWeekCount (boolean; optional)

- footerToolbar (dict | boolean; optional)

- handleWindowResize (boolean; optional)

- headerToolbar (dict | boolean; optional)

- height (number | string; optional)

- hiddenDays (list; optional)

- initialDate (string; optional)

- initialView (string; optional)

- lazyFetching (boolean; optional)

- listDayFormat (dict | string | boolean; optional)

- listDaySideFormat (dict | string | boolean; optional)

- locale (string; optional)

- locales (list; optional)

- longPressDelay (number; optional)

- moreLinkClassNames (list | dict | string; optional)

- moreLinkClick (string; optional)

- moreLinkContent (a list of or a singular dash component, string or number; optional)

- moreLinkText (string; optional)

- multiMonthMaxColumns (number; optional)

- multiMonthMinWidth (number; optional)

- multiMonthTitleFormat (dict | string; optional)

- navLinkDayClick (string; optional)

- navLinkHint (string; optional)

- navLinkWeekClick (string; optional)

- navLinks (boolean; optional)

- nextDayThreshold (string | dict; optional)

- noEventsClassNames (list | dict | string; optional)

- noEventsContent (a list of or a singular dash component, string or number; optional)

- now (string; optional)

- nowIndicator (boolean; optional)

- progressiveEventRendering (boolean; optional)

- rerenderDelay (number; optional)

- scrollTime (string | dict; optional)

- scrollTimeReset (boolean; optional)

- select (boolean | number | string | dict | list; optional):
    Object containing the selected range information, for use in Dash
    callbacks.

- selectConstraint (dict | string; optional)

- selectLongPressDelay (number; optional)

- selectMinDistance (number; optional)

- selectMirror (boolean; optional)

- selectOverlap (boolean; optional)

- selectable (boolean; optional)

- showNonCurrentDates (boolean; optional)

- slotDuration (string | dict; optional)

- slotLabelClassNames (list | dict | string; optional)

- slotLabelContent (a list of or a singular dash component, string or number; optional)

- slotLabelFormat (list | dict | string; optional)

- slotLabelInterval (string | dict; optional)

- slotLaneClassNames (list | dict | string; optional)

- slotLaneContent (a list of or a singular dash component, string or number; optional)

- slotMaxTime (string | dict; optional)

- slotMinTime (string | dict; optional)

- slotMinWidth (number; optional)

- snapDuration (string | dict; optional)

- startParam (string; optional)

- stickyFooterScrollbar (boolean; optional)

- stickyHeaderDates (boolean; optional)

- themeSystem (string; optional)

- timeZoneParam (string; optional)

- titleFormat (dict | string; optional)

- unselect (boolean | number | string | dict | list; optional):
    Flag indicating unselection occurred, for use in Dash callbacks.

- unselectAuto (boolean; optional)

- unselectCancel (string; optional)

- validRange (dict; optional)

- viewClassNames (list | dict | string; optional)

- views (dict; optional)

- weekNumberCalculation (string; optional)

- weekNumberFormat (dict | string; optional)

- weekNumbers (boolean; optional)

- weekText (string; optional)

- weekTextLong (string; optional)

- weekends (boolean; optional)

- windowResizeDelay (number; optional)"""
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
