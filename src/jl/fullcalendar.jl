# AUTO GENERATED FILE - DO NOT EDIT

export fullcalendar

"""
    fullcalendar(;kwargs...)

A FullCalendar component.
DashFullCalendar – thin Dash wrapper around @fullcalendar/react.
ALL props (except the Dash house‑keeping ones) are forwarded verbatim.
No monkey‑patching of FullCalendar internals.
Keyword arguments:
- `id` (String; optional): Unique HTML id for the calendar container.  See FullCalendar docs.
- `allDayClassNames` (Array | Dict | String; optional): Class names for the all-day row.  See FullCalendar docs.
- `allDayContent` (a list of or a singular dash component, string or number; optional): Custom renderer for the all-day cell.  See FullCalendar docs.
- `allDaySlot` (Bool; optional): Display the all-day row in time-grid views.  See FullCalendar docs.
- `allDayText` (String; optional): Text label for the all-day slot.  See FullCalendar docs.
- `aspectRatio` (Real; optional): Width/height ratio when `height` is auto.  See FullCalendar docs.
- `businessHours` (Bool | Dict | Array; optional): Business-hours definition(s) or `true` for default.  See FullCalendar docs.
- `buttonIcons` (Dict; optional): Icon class strings mapped to built-in button names.  See FullCalendar docs.
- `buttonText` (Dict; optional): Override text labels for built-in buttons.  See FullCalendar docs.
- `command` (Dict; optional): An object specifying a command to execute on the calendar API, such as {'type': 'next'} to navigate to the next period.
- `contentHeight` (Real | String; optional): Height of the scrollable content area.  See FullCalendar docs.
- `customButtons` (Dict; optional): Custom button definitions keyed by name.  See FullCalendar docs.
- `dateClick` (Bool | Real | String | Dict | Array; optional): The date string of the clicked date, for use in Dash callbacks.
- `datesSet` (Bool | Real | String | Dict | Array; optional): Object containing the current date range, for use in Dash callbacks.
- `dayCellClassNames` (Array | Dict | String; optional): Class names for day cells.  See FullCalendar docs.
- `dayCellContent` (a list of or a singular dash component, string or number; optional): Custom renderer for day cells.  See FullCalendar docs.
- `dayHeaderClassNames` (Array | Dict | String; optional): Class names for day headers.  See FullCalendar docs.
- `dayHeaderContent` (a list of or a singular dash component, string or number; optional): Custom renderer for day headers.  See FullCalendar docs.
- `dayHeaderFormat` (Dict | String; optional): Formatter for day-header text.  See FullCalendar docs.
- `dayMaxEventRows` (Bool | Real; optional): Alternate way to cap events per day (rows).  See FullCalendar docs.
- `dayMaxEvents` (Bool | Real; optional): Collapse rows after this many events per day.  See FullCalendar docs.
- `dayMinWidth` (Real; optional): Minimum pixel width of a day column.  See FullCalendar docs.
- `dayPopoverFormat` (Dict | String; optional): Date-format skeleton for the day popover.  See FullCalendar docs.
- `defaultAllDay` (Bool; optional): Default all-day status for new events.  See FullCalendar docs.
- `dir` (String; optional): Text direction: ‘ltr’ or ‘rtl’.  See FullCalendar docs.
- `displayEventEnd` (Bool; optional): Show event end time.  See FullCalendar docs.
- `displayEventTime` (Bool; optional): Show event time.  See FullCalendar docs.
- `dragRevertDuration` (Real; optional): Duration for drag revert animation.  See FullCalendar docs.
- `dragScroll` (Bool; optional): Allow calendar to scroll during drag.  See FullCalendar docs.
- `dropAccept` (String; optional): Selector or function to accept drops.  See FullCalendar docs.
- `droppable` (Bool; optional): Allow external elements to be dropped.  See FullCalendar docs.
- `editable` (Bool; optional): Allow events to be editable.  See FullCalendar docs.
- `endParam` (String; optional): Name of end date GET param.  See FullCalendar docs.
- `eventAdd` (Bool | Real | String | Dict | Array; optional): Object containing information about the added event, for use in Dash callbacks.
- `eventBackgroundColor` (String; optional): Default background color for events.  See FullCalendar docs.
- `eventBorderColor` (String; optional): Default border color for events.  See FullCalendar docs.
- `eventChange` (Bool | Real | String | Dict | Array; optional): Object containing information about the changed event, for use in Dash callbacks.
- `eventClassNames` (Array | Dict | String; optional): Class names for events.  See FullCalendar docs.
- `eventClick` (Bool | Real | String | Dict | Array; optional): Object containing information about the clicked event, for use in Dash callbacks.
- `eventColor` (String; optional): Default color for events.  See FullCalendar docs.
- `eventConstraint` (Dict | String; optional): Event constraint for dragging/resizing.  See FullCalendar docs.
- `eventContent` (a list of or a singular dash component, string or number; optional): Custom renderer for events.  See FullCalendar docs.
- `eventDisplay` (String; optional): Rendering style for events.  See FullCalendar docs.
- `eventDrop` (Bool | Real | String | Dict | Array; optional): Object containing information about the dropped event, for use in Dash callbacks.
- `eventDurationEditable` (Bool; optional): Allow event duration to be editable.  See FullCalendar docs.
- `eventLongPressDelay` (Real; optional): Delay for event long press (ms).  See FullCalendar docs.
- `eventOrder` (Array | String; optional): Determines event sort order.  See FullCalendar docs.
- `eventOrderStrict` (Bool; optional): Enforce strict event ordering.  See FullCalendar docs.
- `eventOverlap` (Bool; optional): Allow events to overlap.  See FullCalendar docs.
- `eventRemove` (Bool | Real | String | Dict | Array; optional): Object containing information about the removed event, for use in Dash callbacks.
- `eventResizableFromStart` (Bool; optional): Allow resizing events from start.  See FullCalendar docs.
- `eventResize` (Bool | Real | String | Dict | Array; optional): Object containing information about the resized event, for use in Dash callbacks.
- `eventSources` (Array; optional): Array of event source objects.  See FullCalendar docs.
- `eventStartEditable` (Bool; optional): Allow event start to be editable.  See FullCalendar docs.
- `eventTextColor` (String; optional): Default text color for events.  See FullCalendar docs.
- `eventTimeFormat` (Dict | String; optional): Formatter for event time text.  See FullCalendar docs.
- `events` (Array | String; optional): Array, URL, or function that supplies the initial events.  See FullCalendar docs.
- `eventsSet` (Bool | Real | String | Dict | Array; optional): Array of current event objects in the calendar, for use in Dash callbacks.
- `expandRows` (Bool; optional): When `true`, rows stretch to fill vertical space.  See FullCalendar docs.
- `firstDay` (Real; optional): Index of week’s first day (0=Sunday).  See FullCalendar docs.
- `fixedWeekCount` (Bool; optional): Always render 6 weeks in month view.  See FullCalendar docs.
- `footerToolbar` (Dict | Bool; optional): Config for the bottom toolbar; set `false` to hide.  See FullCalendar docs.
- `handleWindowResize` (Bool; optional): Recompute dimensions on window resize.  See FullCalendar docs.
- `headerToolbar` (Dict | Bool; optional): Config for the top toolbar; set `false` to hide.  See FullCalendar docs.
- `height` (Real | String; optional): Overall calendar height (`number`, ‘auto’, ‘parent’, or function).  See FullCalendar docs.
- `hiddenDays` (Array; optional): Array of day numbers to hide (0=Sun).  See FullCalendar docs.
- `initialDate` (String; optional): Date the calendar navigates to on first render.  See FullCalendar docs.
- `initialView` (String; optional): Name of the view the calendar shows on first load.  See FullCalendar docs.
- `lazyFetching` (Bool; optional): Fetch events only when needed.  See FullCalendar docs.
- `listDayFormat` (Dict | String | Bool; optional): Formatter for list view group headers.  See FullCalendar docs.
- `listDaySideFormat` (Dict | String | Bool; optional): Formatter for list view side headers.  See FullCalendar docs.
- `locale` (String; optional): Calendar locale code (e.g. ‘en-gb’).  See FullCalendar docs.
- `locales` (Array; optional): Array of additional locale objects to load.  See FullCalendar docs.
- `longPressDelay` (Real; optional): Delay for long press (ms).  See FullCalendar docs.
- `moreLinkClassNames` (Array | Dict | String; optional): Class names for the ‘+ more’ link.  See FullCalendar docs.
- `moreLinkClick` (String; optional): Action when a ‘+ more’ link is clicked.  See FullCalendar docs.
- `moreLinkContent` (a list of or a singular dash component, string or number; optional): Custom renderer for the ‘+ more’ link.  See FullCalendar docs.
- `moreLinkText` (String; optional): Text factory for the ‘+ more’ link.  See FullCalendar docs.
- `multiMonthMaxColumns` (Real; optional): Max columns in multi-month view.  See FullCalendar docs.
- `multiMonthMinWidth` (Real; optional): Min width for multi-month columns.  See FullCalendar docs.
- `multiMonthTitleFormat` (Dict | String; optional): Title format for multi-month view.  See FullCalendar docs.
- `navLinkDayClick` (String; optional): Handler for day navigation link clicks.  See FullCalendar docs.
- `navLinkHint` (String; optional): Tooltip for navigation links.  See FullCalendar docs.
- `navLinkWeekClick` (String; optional): Handler for week navigation link clicks.  See FullCalendar docs.
- `navLinks` (Bool; optional): Enable day/week navigation links.  See FullCalendar docs.
- `nextDayThreshold` (String | Dict; optional): Threshold for "next day" calculation.  See FullCalendar docs.
- `noEventsClassNames` (Array | Dict | String; optional): Class names applied when no events are present.  See FullCalendar docs.
- `noEventsContent` (a list of or a singular dash component, string or number; optional): Custom ‘no events’ content renderer.  See FullCalendar docs.
- `now` (String; optional): Function/string/Date returning the ‘current’ date.  See FullCalendar docs.
- `nowIndicator` (Bool; optional): Render a line marking the current time.  See FullCalendar docs.
- `plugins` (Array of String | Dicts; optional): Additional plugins. Accepts plugin instances (objects/functions) and/or plugin names (strings).
If strings match Premium plugins (e.g., 'scrollgrid', 'resourceTimeline', 'resourceTimeGrid', 'resource'),
they will be lazy-loaded only when `schedulerLicenseKey` is provided. Unknown strings are ignored.
- `progressiveEventRendering` (Bool; optional): Render events as they load.  See FullCalendar docs.
- `rerenderDelay` (Real; optional): Delay before rerendering events.  See FullCalendar docs.
- `schedulerLicenseKey` (String; optional): FullCalendar Premium (Scheduler) license key. Required when using any Premium plugin
such as resource views or scrollgrid. See docs: https://fullcalendar.io/docs/schedulerLicenseKey
- `scrollTime` (String | Dict; optional): Initial scroll position of time-grid views.  See FullCalendar docs.
- `scrollTimeReset` (Bool; optional): Reset scroll position when changing views.  See FullCalendar docs.
- `select` (Bool | Real | String | Dict | Array; optional): Object containing the selected range information, for use in Dash callbacks.
- `selectConstraint` (Dict | String; optional): Selection constraint for selecting.  See FullCalendar docs.
- `selectLongPressDelay` (Real; optional): Delay for select long press (ms).  See FullCalendar docs.
- `selectMinDistance` (Real; optional): Minimum drag distance before selection.  See FullCalendar docs.
- `selectMirror` (Bool; optional): Show a mirror of selection while dragging.  See FullCalendar docs.
- `selectOverlap` (Bool; optional): Allow selection to overlap events.  See FullCalendar docs.
- `selectable` (Bool; optional): Allow date/time range selection.  See FullCalendar docs.
- `showNonCurrentDates` (Bool; optional): Render leading/trailing days in month view.  See FullCalendar docs.
- `slotDuration` (String | Dict; optional): Granularity of the vertical time slots.  See FullCalendar docs.
- `slotLabelClassNames` (Array | Dict | String; optional): Class names for slot labels.  See FullCalendar docs.
- `slotLabelContent` (a list of or a singular dash component, string or number; optional): Custom renderer for slot labels.  See FullCalendar docs.
- `slotLabelFormat` (Array | Dict | String; optional): Formatter(s) for slot labels.  See FullCalendar docs.
- `slotLabelInterval` (String | Dict; optional): Interval between slot labels.  See FullCalendar docs.
- `slotLaneClassNames` (Array | Dict | String; optional): Class names for resource lanes.  See FullCalendar docs.
- `slotLaneContent` (a list of or a singular dash component, string or number; optional): Custom renderer for resource lanes.  See FullCalendar docs.
- `slotMaxTime` (String | Dict; optional): Latest time shown on a day.  See FullCalendar docs.
- `slotMinTime` (String | Dict; optional): Earliest time shown on a day.  See FullCalendar docs.
- `slotMinWidth` (Real; optional): Minimum pixel width of a resource column.  See FullCalendar docs.
- `snapDuration` (String | Dict; optional): Grid snapping interval while dragging.  See FullCalendar docs.
- `startParam` (String; optional): Name of start date GET param.  See FullCalendar docs.
- `stickyFooterScrollbar` (Bool; optional): Show sticky scrollbar at the bottom.  See FullCalendar docs.
- `stickyHeaderDates` (Bool; optional): Keep date headers fixed while scrolling.  See FullCalendar docs.
- `themeSystem` (String; optional): Theme system to apply to built-in UI (e.g. ‘standard’, ‘bootstrap5’).  See FullCalendar docs.
- `timeZoneParam` (String; optional): Name of time zone GET param.  See FullCalendar docs.
- `titleFormat` (Dict | String; optional): Date-formatting skeleton or object for the view title.  See FullCalendar docs.
- `unselect` (Bool | Real | String | Dict | Array; optional): Flag indicating unselection occurred, for use in Dash callbacks.
- `unselectAuto` (Bool; optional): Unselect when clicking outside.  See FullCalendar docs.
- `unselectCancel` (String; optional): CSS selector for elements that prevent unselect.  See FullCalendar docs.
- `validRange` (Dict; optional): Restricts navigation/selection to a date range.  See FullCalendar docs.
- `viewClassNames` (Array | Dict | String; optional): Class names for the view container.  See FullCalendar docs.
- `views` (Dict; optional): Custom view definitions mapped by name.  See FullCalendar docs.
- `weekNumberCalculation` (String; optional): Custom week-number algorithm.  See FullCalendar docs.
- `weekNumberFormat` (Dict | String; optional): Formatter for week-number text.  See FullCalendar docs.
- `weekNumbers` (Bool; optional): Show ISO week numbers down the side.  See FullCalendar docs.
- `weekText` (String; optional): Short label preceding week numbers.  See FullCalendar docs.
- `weekTextLong` (String; optional): Long label preceding week numbers.  See FullCalendar docs.
- `weekends` (Bool; optional): Show weekend columns.  See FullCalendar docs.
- `windowResizeDelay` (Real; optional): Debounce (ms) for the resize handler.  See FullCalendar docs.
"""
function fullcalendar(; kwargs...)
        available_props = Symbol[:id, :allDayClassNames, :allDayContent, :allDaySlot, :allDayText, :aspectRatio, :businessHours, :buttonIcons, :buttonText, :command, :contentHeight, :customButtons, :dateClick, :datesSet, :dayCellClassNames, :dayCellContent, :dayHeaderClassNames, :dayHeaderContent, :dayHeaderFormat, :dayMaxEventRows, :dayMaxEvents, :dayMinWidth, :dayPopoverFormat, :defaultAllDay, :dir, :displayEventEnd, :displayEventTime, :dragRevertDuration, :dragScroll, :dropAccept, :droppable, :editable, :endParam, :eventAdd, :eventBackgroundColor, :eventBorderColor, :eventChange, :eventClassNames, :eventClick, :eventColor, :eventConstraint, :eventContent, :eventDisplay, :eventDrop, :eventDurationEditable, :eventLongPressDelay, :eventOrder, :eventOrderStrict, :eventOverlap, :eventRemove, :eventResizableFromStart, :eventResize, :eventSources, :eventStartEditable, :eventTextColor, :eventTimeFormat, :events, :eventsSet, :expandRows, :firstDay, :fixedWeekCount, :footerToolbar, :handleWindowResize, :headerToolbar, :height, :hiddenDays, :initialDate, :initialView, :lazyFetching, :listDayFormat, :listDaySideFormat, :locale, :locales, :longPressDelay, :moreLinkClassNames, :moreLinkClick, :moreLinkContent, :moreLinkText, :multiMonthMaxColumns, :multiMonthMinWidth, :multiMonthTitleFormat, :navLinkDayClick, :navLinkHint, :navLinkWeekClick, :navLinks, :nextDayThreshold, :noEventsClassNames, :noEventsContent, :now, :nowIndicator, :plugins, :progressiveEventRendering, :rerenderDelay, :schedulerLicenseKey, :scrollTime, :scrollTimeReset, :select, :selectConstraint, :selectLongPressDelay, :selectMinDistance, :selectMirror, :selectOverlap, :selectable, :showNonCurrentDates, :slotDuration, :slotLabelClassNames, :slotLabelContent, :slotLabelFormat, :slotLabelInterval, :slotLaneClassNames, :slotLaneContent, :slotMaxTime, :slotMinTime, :slotMinWidth, :snapDuration, :startParam, :stickyFooterScrollbar, :stickyHeaderDates, :themeSystem, :timeZoneParam, :titleFormat, :unselect, :unselectAuto, :unselectCancel, :validRange, :viewClassNames, :views, :weekNumberCalculation, :weekNumberFormat, :weekNumbers, :weekText, :weekTextLong, :weekends, :windowResizeDelay]
        wild_props = Symbol[]
        return Component("fullcalendar", "FullCalendar", "dash_fullcalendar", available_props, wild_props; kwargs...)
end

