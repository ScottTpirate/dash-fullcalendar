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
nowIndicator=NULL, progressiveEventRendering=NULL,
rerenderDelay=NULL, scrollTime=NULL, scrollTimeReset=NULL,
select=NULL, selectAllow=NULL, selectConstraint=NULL,
selectLongPressDelay=NULL, selectMinDistance=NULL,
selectMirror=NULL, selectOverlap=NULL, selectable=NULL,
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
\item{id}{Character. }

\item{allDayClassNames}{Unnamed list | named list | character. }

\item{allDayContent}{A list of or a singular dash component, string or number. }

\item{allDayDidMount}{}

\item{allDaySlot}{Logical. }

\item{allDayText}{Character. }

\item{allDayWillUnmount}{}

\item{aspectRatio}{Numeric. }

\item{businessHours}{Logical | named list | unnamed list. }

\item{buttonIcons}{Named list. }

\item{buttonText}{Named list. }

\item{command}{Named list. An object specifying a command to execute on the calendar API, such as {'type': 'next'} to navigate to the next period.}

\item{contentHeight}{Numeric | character. }

\item{customButtons}{Named list. }

\item{dateClick}{Logical | numeric | character | named list | unnamed list. The date string of the clicked date, for use in Dash callbacks.}

\item{datesSet}{Logical | numeric | character | named list | unnamed list. Object containing the current date range, for use in Dash callbacks.}

\item{dayCellClassNames}{Unnamed list | named list | character. }

\item{dayCellContent}{A list of or a singular dash component, string or number. }

\item{dayCellDidMount}{}

\item{dayCellWillUnmount}{}

\item{dayHeaderClassNames}{Unnamed list | named list | character. }

\item{dayHeaderContent}{A list of or a singular dash component, string or number. }

\item{dayHeaderDidMount}{}

\item{dayHeaderFormat}{Named list | character. }

\item{dayHeaderWillUnmount}{}

\item{dayMaxEventRows}{Logical | numeric. }

\item{dayMaxEvents}{Logical | numeric. }

\item{dayMinWidth}{Numeric. }

\item{dayPopoverFormat}{Named list | character. }

\item{defaultAllDay}{Logical. }

\item{dir}{Character. }

\item{displayEventEnd}{Logical. }

\item{displayEventTime}{Logical. }

\item{dragRevertDuration}{Numeric. }

\item{dragScroll}{Logical. }

\item{drop}{}

\item{dropAccept}{Character. }

\item{droppable}{Logical. }

\item{editable}{Logical. }

\item{endParam}{Character. }

\item{eventAdd}{Logical | numeric | character | named list | unnamed list. Object containing information about the added event, for use in Dash callbacks.}

\item{eventAllow}{}

\item{eventBackgroundColor}{Character. }

\item{eventBorderColor}{Character. }

\item{eventChange}{Logical | numeric | character | named list | unnamed list. Object containing information about the changed event, for use in Dash callbacks.}

\item{eventClassNames}{Unnamed list | named list | character. }

\item{eventClick}{Logical | numeric | character | named list | unnamed list. Object containing information about the clicked event, for use in Dash callbacks.}

\item{eventColor}{Character. }

\item{eventConstraint}{Named list | character. }

\item{eventContent}{A list of or a singular dash component, string or number. }

\item{eventDataTransform}{}

\item{eventDidMount}{}

\item{eventDisplay}{Character. }

\item{eventDragStart}{}

\item{eventDragStop}{}

\item{eventDrop}{Logical | numeric | character | named list | unnamed list. Object containing information about the dropped event, for use in Dash callbacks.}

\item{eventDurationEditable}{Logical. }

\item{eventLeave}{}

\item{eventLongPressDelay}{Numeric. }

\item{eventMouseEnter}{}

\item{eventMouseLeave}{}

\item{eventOrder}{Unnamed list | character. }

\item{eventOrderStrict}{Logical. }

\item{eventOverlap}{Logical. }

\item{eventReceive}{}

\item{eventRemove}{Logical | numeric | character | named list | unnamed list. Object containing information about the removed event, for use in Dash callbacks.}

\item{eventResizableFromStart}{Logical. }

\item{eventResize}{Logical | numeric | character | named list | unnamed list. Object containing information about the resized event, for use in Dash callbacks.}

\item{eventResizeStart}{}

\item{eventResizeStop}{}

\item{eventSources}{Unnamed list. }

\item{eventStartEditable}{Logical. }

\item{eventTextColor}{Character. }

\item{eventTimeFormat}{Named list | character. }

\item{eventWillUnmount}{}

\item{events}{Unnamed list | character. }

\item{eventsSet}{Logical | numeric | character | named list | unnamed list. Array of current event objects in the calendar, for use in Dash callbacks.}

\item{expandRows}{Logical. }

\item{firstDay}{Numeric. }

\item{fixedWeekCount}{Logical. }

\item{footerToolbar}{Named list | logical. }

\item{handleWindowResize}{Logical. }

\item{headerToolbar}{Named list | logical. }

\item{height}{Numeric | character. }

\item{hiddenDays}{Unnamed list. }

\item{initialDate}{Character. }

\item{initialView}{Character. }

\item{lazyFetching}{Logical. }

\item{listDayFormat}{Named list | character | logical. }

\item{listDaySideFormat}{Named list | character | logical. }

\item{loading}{}

\item{locale}{Character. }

\item{locales}{Unnamed list. }

\item{longPressDelay}{Numeric. }

\item{moreLinkClassNames}{Unnamed list | named list | character. }

\item{moreLinkClick}{Character. }

\item{moreLinkContent}{A list of or a singular dash component, string or number. }

\item{moreLinkDidMount}{}

\item{moreLinkText}{Character. }

\item{moreLinkWillUnmount}{}

\item{multiMonthMaxColumns}{Numeric. }

\item{multiMonthMinWidth}{Numeric. }

\item{multiMonthTitleFormat}{Named list | character. }

\item{navLinkDayClick}{Character. }

\item{navLinkHint}{Character. }

\item{navLinkWeekClick}{Character. }

\item{navLinks}{Logical. }

\item{nextDayThreshold}{Character | named list. }

\item{noEventsClassNames}{Unnamed list | named list | character. }

\item{noEventsContent}{A list of or a singular dash component, string or number. }

\item{noEventsDidMount}{}

\item{noEventsWillUnmount}{}

\item{now}{Character. }

\item{nowIndicator}{Logical. }

\item{progressiveEventRendering}{Logical. }

\item{rerenderDelay}{Numeric. }

\item{scrollTime}{Character | named list. }

\item{scrollTimeReset}{Logical. }

\item{select}{Logical | numeric | character | named list | unnamed list. Object containing the selected range information, for use in Dash callbacks.}

\item{selectAllow}{}

\item{selectConstraint}{Named list | character. }

\item{selectLongPressDelay}{Numeric. }

\item{selectMinDistance}{Numeric. }

\item{selectMirror}{Logical. }

\item{selectOverlap}{Logical. }

\item{selectable}{Logical. }

\item{showNonCurrentDates}{Logical. }

\item{slotDuration}{Character | named list. }

\item{slotLabelClassNames}{Unnamed list | named list | character. }

\item{slotLabelContent}{A list of or a singular dash component, string or number. }

\item{slotLabelDidMount}{}

\item{slotLabelFormat}{Unnamed list | named list | character. }

\item{slotLabelInterval}{Character | named list. }

\item{slotLabelWillUnmount}{}

\item{slotLaneClassNames}{Unnamed list | named list | character. }

\item{slotLaneContent}{A list of or a singular dash component, string or number. }

\item{slotLaneDidMount}{}

\item{slotLaneWillUnmount}{}

\item{slotMaxTime}{Character | named list. }

\item{slotMinTime}{Character | named list. }

\item{slotMinWidth}{Numeric. }

\item{snapDuration}{Character | named list. }

\item{startParam}{Character. }

\item{stickyFooterScrollbar}{Logical. }

\item{stickyHeaderDates}{Logical. }

\item{themeSystem}{Character. }

\item{timeZoneParam}{Character. }

\item{titleFormat}{Named list | character. }

\item{unselect}{Logical | numeric | character | named list | unnamed list. Flag indicating unselection occurred, for use in Dash callbacks.}

\item{unselectAuto}{Logical. }

\item{unselectCancel}{Character. }

\item{validRange}{Named list. }

\item{viewClassNames}{Unnamed list | named list | character. }

\item{viewDidMount}{}

\item{viewWillUnmount}{}

\item{views}{Named list. }

\item{visibleRange}{}

\item{weekNumberCalculation}{Character. }

\item{weekNumberFormat}{Named list | character. }

\item{weekNumbers}{Logical. }

\item{weekText}{Character. }

\item{weekTextLong}{Character. }

\item{weekends}{Logical. }

\item{windowResizeDelay}{Numeric. }
}

\value{named list of JSON elements corresponding to React.js properties and their values}

