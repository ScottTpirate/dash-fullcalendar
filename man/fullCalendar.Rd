% Auto-generated: do not edit by hand
\name{fullCalendar}

\alias{fullCalendar}

\title{FullCalendar component}

\description{
DashFullCalendar – thin Dash wrapper around @fullcalendar/react. ALL props (except the Dash house‑keeping ones) are forwarded verbatim. No monkey‑patching of FullCalendar internals.
}

\usage{
fullCalendar(id=NULL, allDayClassNames=NULL, allDayContent=NULL,
allDayDidMount=NULL, allDaySlot=NULL, allDayText=NULL,
allDayWillUnmount=NULL, aspectRatio=NULL,
businessHours=NULL, buttonIcons=NULL, buttonText=NULL,
command=NULL, contentHeight=NULL, customButtons=NULL,
dateClick=NULL, datesSet=NULL, dayCellClassNames=NULL,
dayCellContent=NULL, dayCellDidMount=NULL,
dayCellWillUnmount=NULL, dayHeaderClassNames=NULL,
dayHeaderContent=NULL, dayHeaderDidMount=NULL,
dayHeaderFormat=NULL, dayHeaderWillUnmount=NULL,
dayMaxEventRows=NULL, dayMaxEvents=NULL, dayMinWidth=NULL,
dayPopoverFormat=NULL, defaultAllDay=NULL, dir=NULL,
displayEventEnd=NULL, displayEventTime=NULL,
dragRevertDuration=NULL, dragScroll=NULL, drop=NULL,
dropAccept=NULL, droppable=NULL, editable=NULL,
endParam=NULL, eventAdd=NULL, eventAllow=NULL,
eventBackgroundColor=NULL, eventBorderColor=NULL,
eventChange=NULL, eventClassNames=NULL, eventClick=NULL,
eventColor=NULL, eventConstraint=NULL, eventContent=NULL,
eventDataTransform=NULL, eventDidMount=NULL,
eventDisplay=NULL, eventDragStart=NULL, eventDragStop=NULL,
eventDrop=NULL, eventDurationEditable=NULL, eventLeave=NULL,
eventLongPressDelay=NULL, eventMouseEnter=NULL,
eventMouseLeave=NULL, eventOrder=NULL,
eventOrderStrict=NULL, eventOverlap=NULL, eventReceive=NULL,
eventRemove=NULL, eventResizableFromStart=NULL,
eventResize=NULL, eventResizeStart=NULL,
eventResizeStop=NULL, eventSources=NULL,
eventStartEditable=NULL, eventTextColor=NULL,
eventTimeFormat=NULL, eventWillUnmount=NULL, events=NULL,
eventsSet=NULL, expandRows=NULL, firstDay=NULL,
fixedWeekCount=NULL, footerToolbar=NULL,
handleWindowResize=NULL, headerToolbar=NULL, height=NULL,
hiddenDays=NULL, initialDate=NULL, initialView=NULL,
lazyFetching=NULL, listDayFormat=NULL,
listDaySideFormat=NULL, loading=NULL, locale=NULL,
locales=NULL, longPressDelay=NULL, moreLinkClassNames=NULL,
moreLinkClick=NULL, moreLinkContent=NULL,
moreLinkDidMount=NULL, moreLinkText=NULL,
moreLinkWillUnmount=NULL, multiMonthMaxColumns=NULL,
multiMonthMinWidth=NULL, multiMonthTitleFormat=NULL,
navLinkDayClick=NULL, navLinkHint=NULL,
navLinkWeekClick=NULL, navLinks=NULL, nextDayThreshold=NULL,
noEventsClassNames=NULL, noEventsContent=NULL,
noEventsDidMount=NULL, noEventsWillUnmount=NULL, now=NULL,
nowIndicator=NULL, plugins=NULL,
progressiveEventRendering=NULL, rerenderDelay=NULL,
schedulerLicenseKey=NULL, scrollTime=NULL,
scrollTimeReset=NULL, select=NULL, selectAllow=NULL,
selectConstraint=NULL, selectLongPressDelay=NULL,
selectMinDistance=NULL, selectMirror=NULL,
selectOverlap=NULL, selectable=NULL,
showNonCurrentDates=NULL, slotDuration=NULL,
slotLabelClassNames=NULL, slotLabelContent=NULL,
slotLabelDidMount=NULL, slotLabelFormat=NULL,
slotLabelInterval=NULL, slotLabelWillUnmount=NULL,
slotLaneClassNames=NULL, slotLaneContent=NULL,
slotLaneDidMount=NULL, slotLaneWillUnmount=NULL,
slotMaxTime=NULL, slotMinTime=NULL, slotMinWidth=NULL,
snapDuration=NULL, startParam=NULL,
stickyFooterScrollbar=NULL, stickyHeaderDates=NULL,
themeSystem=NULL, timeZoneParam=NULL, titleFormat=NULL,
unselect=NULL, unselectAuto=NULL, unselectCancel=NULL,
validRange=NULL, viewClassNames=NULL, viewDidMount=NULL,
viewWillUnmount=NULL, views=NULL, visibleRange=NULL,
weekNumberCalculation=NULL, weekNumberFormat=NULL,
weekNumbers=NULL, weekText=NULL, weekTextLong=NULL,
weekends=NULL, windowResizeDelay=NULL)
}

\arguments{
\item{id}{Character. Unique HTML id for the calendar container.  See FullCalendar docs.}

\item{allDayClassNames}{Unnamed list | named list | character. Class names for the all-day row.  See FullCalendar docs.}

\item{allDayContent}{A list of or a singular dash component, string or number. Custom renderer for the all-day cell.  See FullCalendar docs.}

\item{allDayDidMount}{Callback after the all-day row mounts.  See FullCalendar docs.}

\item{allDaySlot}{Logical. Display the all-day row in time-grid views.  See FullCalendar docs.}

\item{allDayText}{Character. Text label for the all-day slot.  See FullCalendar docs.}

\item{allDayWillUnmount}{Callback before the all-day row unmounts.  See FullCalendar docs.}

\item{aspectRatio}{Numeric. Width/height ratio when `height` is auto.  See FullCalendar docs.}

\item{businessHours}{Logical | named list | unnamed list. Business-hours definition(s) or `true` for default.  See FullCalendar docs.}

\item{buttonIcons}{Named list. Icon class strings mapped to built-in button names.  See FullCalendar docs.}

\item{buttonText}{Named list. Override text labels for built-in buttons.  See FullCalendar docs.}

\item{command}{Named list. An object specifying a command to execute on the calendar API, such as {'type': 'next'} to navigate to the next period.}

\item{contentHeight}{Numeric | character. Height of the scrollable content area.  See FullCalendar docs.}

\item{customButtons}{Named list. Custom button definitions keyed by name.  See FullCalendar docs.}

\item{dateClick}{Logical | numeric | character | named list | unnamed list. The date string of the clicked date, for use in Dash callbacks.}

\item{datesSet}{Logical | numeric | character | named list | unnamed list. Object containing the current date range, for use in Dash callbacks.}

\item{dayCellClassNames}{Unnamed list | named list | character. Class names for day cells.  See FullCalendar docs.}

\item{dayCellContent}{A list of or a singular dash component, string or number. Custom renderer for day cells.  See FullCalendar docs.}

\item{dayCellDidMount}{Callback after a day cell mounts.  See FullCalendar docs.}

\item{dayCellWillUnmount}{Callback before a day cell unmounts.  See FullCalendar docs.}

\item{dayHeaderClassNames}{Unnamed list | named list | character. Class names for day headers.  See FullCalendar docs.}

\item{dayHeaderContent}{A list of or a singular dash component, string or number. Custom renderer for day headers.  See FullCalendar docs.}

\item{dayHeaderDidMount}{Callback after a day header mounts.  See FullCalendar docs.}

\item{dayHeaderFormat}{Named list | character. Formatter for day-header text.  See FullCalendar docs.}

\item{dayHeaderWillUnmount}{Callback before a day header unmounts.  See FullCalendar docs.}

\item{dayMaxEventRows}{Logical | numeric. Alternate way to cap events per day (rows).  See FullCalendar docs.}

\item{dayMaxEvents}{Logical | numeric. Collapse rows after this many events per day.  See FullCalendar docs.}

\item{dayMinWidth}{Numeric. Minimum pixel width of a day column.  See FullCalendar docs.}

\item{dayPopoverFormat}{Named list | character. Date-format skeleton for the day popover.  See FullCalendar docs.}

\item{defaultAllDay}{Logical. Default all-day status for new events.  See FullCalendar docs.}

\item{dir}{Character. Text direction: ‘ltr’ or ‘rtl’.  See FullCalendar docs.}

\item{displayEventEnd}{Logical. Show event end time.  See FullCalendar docs.}

\item{displayEventTime}{Logical. Show event time.  See FullCalendar docs.}

\item{dragRevertDuration}{Numeric. Duration for drag revert animation.  See FullCalendar docs.}

\item{dragScroll}{Logical. Allow calendar to scroll during drag.  See FullCalendar docs.}

\item{drop}{Callback for drop of external elements.  See FullCalendar docs.}

\item{dropAccept}{Character. Selector or function to accept drops.  See FullCalendar docs.}

\item{droppable}{Logical. Allow external elements to be dropped.  See FullCalendar docs.}

\item{editable}{Logical. Allow events to be editable.  See FullCalendar docs.}

\item{endParam}{Character. Name of end date GET param.  See FullCalendar docs.}

\item{eventAdd}{Logical | numeric | character | named list | unnamed list. Object containing information about the added event, for use in Dash callbacks.}

\item{eventAllow}{Determines if an event can be moved/resized.  See FullCalendar docs.}

\item{eventBackgroundColor}{Character. Default background color for events.  See FullCalendar docs.}

\item{eventBorderColor}{Character. Default border color for events.  See FullCalendar docs.}

\item{eventChange}{Logical | numeric | character | named list | unnamed list. Object containing information about the changed event, for use in Dash callbacks.}

\item{eventClassNames}{Unnamed list | named list | character. Class names for events.  See FullCalendar docs.}

\item{eventClick}{Logical | numeric | character | named list | unnamed list. Object containing information about the clicked event, for use in Dash callbacks.}

\item{eventColor}{Character. Default color for events.  See FullCalendar docs.}

\item{eventConstraint}{Named list | character. Event constraint for dragging/resizing.  See FullCalendar docs.}

\item{eventContent}{A list of or a singular dash component, string or number. Custom renderer for events.  See FullCalendar docs.}

\item{eventDataTransform}{Transform event data before rendering.  See FullCalendar docs.}

\item{eventDidMount}{Callback after an event is mounted.  See FullCalendar docs.}

\item{eventDisplay}{Character. Rendering style for events.  See FullCalendar docs.}

\item{eventDragStart}{Event drag starts.  See FullCalendar docs.}

\item{eventDragStop}{Event drag stops.  See FullCalendar docs.}

\item{eventDrop}{Logical | numeric | character | named list | unnamed list. Object containing information about the dropped event, for use in Dash callbacks.}

\item{eventDurationEditable}{Logical. Allow event duration to be editable.  See FullCalendar docs.}

\item{eventLeave}{Callback when an external event is removed.  See FullCalendar docs.}

\item{eventLongPressDelay}{Numeric. Delay for event long press (ms).  See FullCalendar docs.}

\item{eventMouseEnter}{Mouse enters event.  See FullCalendar docs.}

\item{eventMouseLeave}{Mouse leaves event.  See FullCalendar docs.}

\item{eventOrder}{Unnamed list | character. Determines event sort order.  See FullCalendar docs.}

\item{eventOrderStrict}{Logical. Enforce strict event ordering.  See FullCalendar docs.}

\item{eventOverlap}{Logical. Allow events to overlap.  See FullCalendar docs.}

\item{eventReceive}{Callback when an external event is received.  See FullCalendar docs.}

\item{eventRemove}{Logical | numeric | character | named list | unnamed list. Object containing information about the removed event, for use in Dash callbacks.}

\item{eventResizableFromStart}{Logical. Allow resizing events from start.  See FullCalendar docs.}

\item{eventResize}{Logical | numeric | character | named list | unnamed list. Object containing information about the resized event, for use in Dash callbacks.}

\item{eventResizeStart}{Event resize starts.  See FullCalendar docs.}

\item{eventResizeStop}{Event resize stops.  See FullCalendar docs.}

\item{eventSources}{Unnamed list. Array of event source objects.  See FullCalendar docs.}

\item{eventStartEditable}{Logical. Allow event start to be editable.  See FullCalendar docs.}

\item{eventTextColor}{Character. Default text color for events.  See FullCalendar docs.}

\item{eventTimeFormat}{Named list | character. Formatter for event time text.  See FullCalendar docs.}

\item{eventWillUnmount}{Callback before an event is unmounted.  See FullCalendar docs.}

\item{events}{Unnamed list | character. Array, URL, or function that supplies the initial events.  See FullCalendar docs.}

\item{eventsSet}{Logical | numeric | character | named list | unnamed list. Array of current event objects in the calendar, for use in Dash callbacks.}

\item{expandRows}{Logical. When `true`, rows stretch to fill vertical space.  See FullCalendar docs.}

\item{firstDay}{Numeric. Index of week’s first day (0=Sunday).  See FullCalendar docs.}

\item{fixedWeekCount}{Logical. Always render 6 weeks in month view.  See FullCalendar docs.}

\item{footerToolbar}{Named list | logical. Config for the bottom toolbar; set `false` to hide.  See FullCalendar docs.}

\item{handleWindowResize}{Logical. Recompute dimensions on window resize.  See FullCalendar docs.}

\item{headerToolbar}{Named list | logical. Config for the top toolbar; set `false` to hide.  See FullCalendar docs.}

\item{height}{Numeric | character. Overall calendar height (`number`, ‘auto’, ‘parent’, or function).  See FullCalendar docs.}

\item{hiddenDays}{Unnamed list. Array of day numbers to hide (0=Sun).  See FullCalendar docs.}

\item{initialDate}{Character. Date the calendar navigates to on first render.  See FullCalendar docs.}

\item{initialView}{Character. Name of the view the calendar shows on first load.  See FullCalendar docs.}

\item{lazyFetching}{Logical. Fetch events only when needed.  See FullCalendar docs.}

\item{listDayFormat}{Named list | character | logical. Formatter for list view group headers.  See FullCalendar docs.}

\item{listDaySideFormat}{Named list | character | logical. Formatter for list view side headers.  See FullCalendar docs.}

\item{loading}{Callback for loading state.  See FullCalendar docs.}

\item{locale}{Character. Calendar locale code (e.g. ‘en-gb’).  See FullCalendar docs.}

\item{locales}{Unnamed list. Array of additional locale objects to load.  See FullCalendar docs.}

\item{longPressDelay}{Numeric. Delay for long press (ms).  See FullCalendar docs.}

\item{moreLinkClassNames}{Unnamed list | named list | character. Class names for the ‘+ more’ link.  See FullCalendar docs.}

\item{moreLinkClick}{Character. Action when a ‘+ more’ link is clicked.  See FullCalendar docs.}

\item{moreLinkContent}{A list of or a singular dash component, string or number. Custom renderer for the ‘+ more’ link.  See FullCalendar docs.}

\item{moreLinkDidMount}{Callback after the ‘+ more’ link mounts.  See FullCalendar docs.}

\item{moreLinkText}{Character. Text factory for the ‘+ more’ link.  See FullCalendar docs.}

\item{moreLinkWillUnmount}{Callback before the ‘+ more’ link unmounts.  See FullCalendar docs.}

\item{multiMonthMaxColumns}{Numeric. Max columns in multi-month view.  See FullCalendar docs.}

\item{multiMonthMinWidth}{Numeric. Min width for multi-month columns.  See FullCalendar docs.}

\item{multiMonthTitleFormat}{Named list | character. Title format for multi-month view.  See FullCalendar docs.}

\item{navLinkDayClick}{Character. Handler for day navigation link clicks.  See FullCalendar docs.}

\item{navLinkHint}{Character. Tooltip for navigation links.  See FullCalendar docs.}

\item{navLinkWeekClick}{Character. Handler for week navigation link clicks.  See FullCalendar docs.}

\item{navLinks}{Logical. Enable day/week navigation links.  See FullCalendar docs.}

\item{nextDayThreshold}{Character | named list. Threshold for "next day" calculation.  See FullCalendar docs.}

\item{noEventsClassNames}{Unnamed list | named list | character. Class names applied when no events are present.  See FullCalendar docs.}

\item{noEventsContent}{A list of or a singular dash component, string or number. Custom ‘no events’ content renderer.  See FullCalendar docs.}

\item{noEventsDidMount}{Callback after ‘no events’ content mounts.  See FullCalendar docs.}

\item{noEventsWillUnmount}{Callback before ‘no events’ content unmounts.  See FullCalendar docs.}

\item{now}{Character. Function/string/Date returning the ‘current’ date.  See FullCalendar docs.}

\item{nowIndicator}{Logical. Render a line marking the current time.  See FullCalendar docs.}

\item{plugins}{List of character | named lists. Additional plugins. Accepts plugin instances (objects/functions) and/or plugin names (strings).
If strings match Premium plugins (e.g., 'scrollgrid', 'resourceTimeline', 'resourceTimeGrid', 'resource'),
they will be lazy-loaded only when `schedulerLicenseKey` is provided. Unknown strings are ignored.}

\item{progressiveEventRendering}{Logical. Render events as they load.  See FullCalendar docs.}

\item{rerenderDelay}{Numeric. Delay before rerendering events.  See FullCalendar docs.}

\item{schedulerLicenseKey}{Character. FullCalendar Premium (Scheduler) license key. Required when using any Premium plugin
such as resource views or scrollgrid. See docs: https://fullcalendar.io/docs/schedulerLicenseKey}

\item{scrollTime}{Character | named list. Initial scroll position of time-grid views.  See FullCalendar docs.}

\item{scrollTimeReset}{Logical. Reset scroll position when changing views.  See FullCalendar docs.}

\item{select}{Logical | numeric | character | named list | unnamed list. Object containing the selected range information, for use in Dash callbacks.}

\item{selectAllow}{Determines if a selection is allowed.  See FullCalendar docs.}

\item{selectConstraint}{Named list | character. Selection constraint for selecting.  See FullCalendar docs.}

\item{selectLongPressDelay}{Numeric. Delay for select long press (ms).  See FullCalendar docs.}

\item{selectMinDistance}{Numeric. Minimum drag distance before selection.  See FullCalendar docs.}

\item{selectMirror}{Logical. Show a mirror of selection while dragging.  See FullCalendar docs.}

\item{selectOverlap}{Logical. Allow selection to overlap events.  See FullCalendar docs.}

\item{selectable}{Logical. Allow date/time range selection.  See FullCalendar docs.}

\item{showNonCurrentDates}{Logical. Render leading/trailing days in month view.  See FullCalendar docs.}

\item{slotDuration}{Character | named list. Granularity of the vertical time slots.  See FullCalendar docs.}

\item{slotLabelClassNames}{Unnamed list | named list | character. Class names for slot labels.  See FullCalendar docs.}

\item{slotLabelContent}{A list of or a singular dash component, string or number. Custom renderer for slot labels.  See FullCalendar docs.}

\item{slotLabelDidMount}{Callback after a slot label mounts.  See FullCalendar docs.}

\item{slotLabelFormat}{Unnamed list | named list | character. Formatter(s) for slot labels.  See FullCalendar docs.}

\item{slotLabelInterval}{Character | named list. Interval between slot labels.  See FullCalendar docs.}

\item{slotLabelWillUnmount}{Callback before a slot label unmounts.  See FullCalendar docs.}

\item{slotLaneClassNames}{Unnamed list | named list | character. Class names for resource lanes.  See FullCalendar docs.}

\item{slotLaneContent}{A list of or a singular dash component, string or number. Custom renderer for resource lanes.  See FullCalendar docs.}

\item{slotLaneDidMount}{Callback after a lane mounts.  See FullCalendar docs.}

\item{slotLaneWillUnmount}{Callback before a lane unmounts.  See FullCalendar docs.}

\item{slotMaxTime}{Character | named list. Latest time shown on a day.  See FullCalendar docs.}

\item{slotMinTime}{Character | named list. Earliest time shown on a day.  See FullCalendar docs.}

\item{slotMinWidth}{Numeric. Minimum pixel width of a resource column.  See FullCalendar docs.}

\item{snapDuration}{Character | named list. Grid snapping interval while dragging.  See FullCalendar docs.}

\item{startParam}{Character. Name of start date GET param.  See FullCalendar docs.}

\item{stickyFooterScrollbar}{Logical. Show sticky scrollbar at the bottom.  See FullCalendar docs.}

\item{stickyHeaderDates}{Logical. Keep date headers fixed while scrolling.  See FullCalendar docs.}

\item{themeSystem}{Character. Theme system to apply to built-in UI (e.g. ‘standard’, ‘bootstrap5’).  See FullCalendar docs.}

\item{timeZoneParam}{Character. Name of time zone GET param.  See FullCalendar docs.}

\item{titleFormat}{Named list | character. Date-formatting skeleton or object for the view title.  See FullCalendar docs.}

\item{unselect}{Logical | numeric | character | named list | unnamed list. Flag indicating unselection occurred, for use in Dash callbacks.}

\item{unselectAuto}{Logical. Unselect when clicking outside.  See FullCalendar docs.}

\item{unselectCancel}{Character. CSS selector for elements that prevent unselect.  See FullCalendar docs.}

\item{validRange}{Named list. Restricts navigation/selection to a date range.  See FullCalendar docs.}

\item{viewClassNames}{Unnamed list | named list | character. Class names for the view container.  See FullCalendar docs.}

\item{viewDidMount}{Callback after a view is mounted.  See FullCalendar docs.}

\item{viewWillUnmount}{Callback before a view is unmounted.  See FullCalendar docs.}

\item{views}{Named list. Custom view definitions mapped by name.  See FullCalendar docs.}

\item{visibleRange}{Precisely set the range of dates shown in a custom view.  See FullCalendar docs.}

\item{weekNumberCalculation}{Character. Custom week-number algorithm.  See FullCalendar docs.}

\item{weekNumberFormat}{Named list | character. Formatter for week-number text.  See FullCalendar docs.}

\item{weekNumbers}{Logical. Show ISO week numbers down the side.  See FullCalendar docs.}

\item{weekText}{Character. Short label preceding week numbers.  See FullCalendar docs.}

\item{weekTextLong}{Character. Long label preceding week numbers.  See FullCalendar docs.}

\item{weekends}{Logical. Show weekend columns.  See FullCalendar docs.}

\item{windowResizeDelay}{Numeric. Debounce (ms) for the resize handler.  See FullCalendar docs.}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

