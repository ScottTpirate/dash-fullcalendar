import React, {useRef, useEffect, useCallback, useState, useMemo} from "react";
import PropTypes from "prop-types";

import FullCalendar from "@fullcalendar/react";
import dayGridPlugin from "@fullcalendar/daygrid";
import timeGridPlugin from "@fullcalendar/timegrid";
import interactionPlugin from "@fullcalendar/interaction";
import listPlugin from "@fullcalendar/list";
import multiMonthPlugin from "@fullcalendar/multimonth";


/**
 * DashFullCalendar – thin Dash wrapper around @fullcalendar/react.
 * ALL props (except the Dash house‑keeping ones) are forwarded verbatim.
 * No monkey‑patching of FullCalendar internals.
 */
const DashFullCalendar = ({
    id,
    setProps,
    command: _command,
    dateClick: _dateClick,
    eventClick: _eventClick,
    select: _select,
    unselect: _unselect,
    eventDrop: _eventDrop,
    eventResize: _eventResize,
    eventAdd: _eventAdd,
    eventChange: _eventChange,
    eventRemove: _eventRemove,
    datesSet: _datesSet,
    eventsSet: _eventsSet,
    schedulerLicenseKey,
    plugins: userPlugins,
    // anything else the user supplies:
    ...calendarProps
}) => {
    const calRef = useRef(null);

    const [premiumPlugins, setPremiumPlugins] = useState([]);

    useEffect(() => {
        let cancelled = false;

        async function loadPremium() {
            const names = Array.isArray(userPlugins)
                ? userPlugins.filter((p) => typeof p === 'string').map((s) => String(s).toLowerCase())
                : [];

            // Map normalized names to @fullcalendar package specifiers (no direct imports here)
            const nameToSpec = {
                scrollgrid: 'scrollgrid',
                resourcetimeline: 'resource-timeline',
                resourcetimegrid: 'resource-timegrid',
                resource: 'resource'
            };

            // Resolve requested Premium specs from provided names
            const requestedSpecs = names
                .map((n) => n.replace(/[-_\s]/g, '').toLowerCase())
                .map((n) => nameToSpec[n])
                .filter(Boolean);

            if (!schedulerLicenseKey || requestedSpecs.length === 0) {
                if (!cancelled) setPremiumPlugins([]);
                return;
            }

            // Dynamic context import so webpack doesn't hard-resolve absent packages at build time
            const loaded = await Promise.all(
                requestedSpecs.map(async (spec) => {
                    try {
                        const mod = await import(
                            /* webpackInclude: /(scrollgrid|resource-timegrid|resource-timeline|resource)$/ */
                            `@fullcalendar/${spec}`
                        );
                        return mod?.default ?? mod;
                    } catch (e) {
                        /* ignore if not present at runtime */
                        return null;
                    }
                })
            );

            if (!cancelled) setPremiumPlugins(loaded.filter(Boolean));
        }

        loadPremium();
        return () => { cancelled = true; };
    }, [userPlugins, schedulerLicenseKey]);

    const userPluginInstances = useMemo(() => (
        Array.isArray(userPlugins) ? userPlugins.filter((p) => typeof p !== 'string') : []
    ), [userPlugins]);

    /* ---------- Utility functions for serialization ---------- */

    const serializeEvent = (event) => ({
        id: event.id,
        groupId: event.groupId,
        allDay: event.allDay,
        startStr: event.startStr,
        endStr: event.endStr,
        title: event.title,
        url: event.url,
        classNames: event.classNames,
        editable: event.editable,
        startEditable: event.startEditable,
        durationEditable: event.durationEditable,
        resourceEditable: event.resourceEditable,
        display: event.display,
        overlap: event.overlap,
        constraint: event.constraint,
        backgroundColor: event.backgroundColor,
        borderColor: event.borderColor,
        textColor: event.textColor,
        extendedProps: event.extendedProps
    });

    const serializeDuration = (delta) => ({
        years: delta.years,
        months: delta.months,
        days: delta.days,
        milliseconds: delta.milliseconds
    });

    /* ---------- Command handling for API methods ---------- */

    useEffect(() => {
        const api = calRef.current?.getApi();
        if (!api || !_command) {return;}

        switch (_command.type) {
            case "next":
                api.next();
                break;
            case "prev":
                api.prev();
                break;
            case "today":
                api.today();
                break;
            case "changeView":
                if (_command.view) {
                    api.changeView(_command.view);
                }
                break;
            // Add more commands as needed
            default:
                // Unknown command
                break;
        }
    }, [_command]);

    /* ---------- Dash ↔ FullCalendar event bridges ---------- */

    const handleDateClick = useCallback(
        (info) => {
            if (setProps) {
                setProps({dateClick: info.dateStr});
            }
        },
        [setProps]
    );

    const handleEventClick = useCallback(
        (info) => {
            if (setProps) {
                setProps({
                    eventClick: {
                        id: info.event.id,
                        title: info.event.title,
                        start: info.event.startStr,
                        end: info.event.endStr,
                        allDay: info.event.allDay,
                        extendedProps: info.event.extendedProps
                    }
                });
            }
        },
        [setProps]
    );

    const handleSelect = useCallback(
        (info) => {
            if (setProps) {
                setProps({
                    select: {
                        start: info.startStr,
                        end: info.endStr,
                        allDay: info.allDay
                    }
                });
            }
        },
        [setProps]
    );

    const handleUnselect = useCallback(
        (info) => {
            if (setProps) {
                setProps({unselect: true});
            }
        },
        [setProps]
    );

    const handleEventDrop = useCallback(
        (info) => {
            if (setProps) {
                setProps({
                    eventDrop: {
                        event: serializeEvent(info.event),
                        oldEvent: serializeEvent(info.oldEvent),
                        delta: serializeDuration(info.delta),
                        relatedEvents: info.relatedEvents.map(serializeEvent)
                    }
                });
            }
        },
        [setProps]
    );

    const handleEventResize = useCallback(
        (info) => {
            if (setProps) {
                setProps({
                    eventResize: {
                        event: serializeEvent(info.event),
                        oldEvent: serializeEvent(info.oldEvent),
                        delta: serializeDuration(info.delta),
                        relatedEvents: info.relatedEvents.map(serializeEvent)
                    }
                });
            }
        },
        [setProps]
    );

    const handleEventAdd = useCallback(
        (arg) => {
            if (setProps) {
                setProps({
                    eventAdd: {
                        event: serializeEvent(arg.event)
                    }
                });
            }
        },
        [setProps]
    );

    const handleEventChange = useCallback(
        (arg) => {
            if (setProps) {
                setProps({
                    eventChange: {
                        event: serializeEvent(arg.event),
                        oldEvent: serializeEvent(arg.oldEvent),
                        relatedEvents: arg.relatedEvents.map(serializeEvent)
                    }
                });
            }
        },
        [setProps]
    );

    const handleEventRemove = useCallback(
        (arg) => {
            if (setProps) {
                setProps({
                    eventRemove: {
                        event: serializeEvent(arg.event),
                        relatedEvents: arg.relatedEvents.map(serializeEvent)
                    }
                });
            }
        },
        [setProps]
    );

    const handleDatesSet = useCallback(
        (info) => {
            if (setProps) {
                setProps({
                    datesSet: {
                        start: info.startStr,
                        end: info.endStr,
                        viewType: info.view.type
                    }
                });
            }
        },
        [setProps]
    );

    const handleEventsSet = useCallback(
        (events) => {
            if (setProps) {
                setProps({
                    eventsSet: events.map(serializeEvent)
                });
            }
        },
        [setProps]
    );

    return (
        <div id={id}>
            <FullCalendar
                ref={calRef}
                plugins={[
                    dayGridPlugin,
                    timeGridPlugin,
                    interactionPlugin,
                    listPlugin,
                    multiMonthPlugin,
                    ...premiumPlugins,
                    ...userPluginInstances
                ]}
                // Always pass the key if provided. Harmless for free plugins; avoids missing key when a user supplies a Premium plugin instance directly.
                {...(schedulerLicenseKey ? { schedulerLicenseKey } : {})}
                {...calendarProps}
                dateClick={handleDateClick}
                eventClick={handleEventClick}
                select={handleSelect}
                unselect={handleUnselect}
                eventDrop={handleEventDrop}
                eventResize={handleEventResize}
                eventAdd={handleEventAdd}
                eventChange={handleEventChange}
                eventRemove={handleEventRemove}
                datesSet={handleDatesSet}
                eventsSet={handleEventsSet}
            />
        </div>
    );
};

/* ---------- Dash mandatory metadata ---------- */

DashFullCalendar.propTypes = {
    /**
     * Unique HTML id for the calendar container.  See FullCalendar docs.
     */
    id: PropTypes.string,

    // Core FullCalendar props (all free edition options, excluding bridged callbacks which are defined below as any)
    /**
     * Name of the view the calendar shows on first load.  See FullCalendar docs.
     */
    initialView: PropTypes.string,
    /**
     * Array, URL, or function that supplies the initial events.  See FullCalendar docs.
     */
    events: PropTypes.oneOfType([
        PropTypes.array,
        PropTypes.string,
        PropTypes.func
    ]),
    /**
     * Config for the top toolbar; set `false` to hide.  See FullCalendar docs.
     */
    headerToolbar: PropTypes.oneOfType([PropTypes.object, PropTypes.bool]),
    /**
     * Config for the bottom toolbar; set `false` to hide.  See FullCalendar docs.
     */
    footerToolbar: PropTypes.oneOfType([PropTypes.object, PropTypes.bool]),
    /**
     * Custom button definitions keyed by name.  See FullCalendar docs.
     */
    customButtons: PropTypes.object,
    /**
     * Icon class strings mapped to built-in button names.  See FullCalendar docs.
     */
    buttonIcons: PropTypes.object,
    /**
     * Override text labels for built-in buttons.  See FullCalendar docs.
     */
    buttonText: PropTypes.object,
    /**
     * Theme system to apply to built-in UI (e.g. ‘standard’, ‘bootstrap5’).  See FullCalendar docs.
     */
    themeSystem: PropTypes.string,
    /**
     * Overall calendar height (`number`, ‘auto’, ‘parent’, or function).  See FullCalendar docs.
     */
    height: PropTypes.oneOfType([PropTypes.number, PropTypes.string, PropTypes.func]),
    /**
     * Height of the scrollable content area.  See FullCalendar docs.
     */
    contentHeight: PropTypes.oneOfType([PropTypes.number, PropTypes.string, PropTypes.func]),
    /**
     * Width/height ratio when `height` is auto.  See FullCalendar docs.
     */
    aspectRatio: PropTypes.number,
    /**
     * When `true`, rows stretch to fill vertical space.  See FullCalendar docs.
     */
    expandRows: PropTypes.bool,
    /**
     * Recompute dimensions on window resize.  See FullCalendar docs.
     */
    handleWindowResize: PropTypes.bool,
    /**
     * Debounce (ms) for the resize handler.  See FullCalendar docs.
     */
    windowResizeDelay: PropTypes.number,
    /**
     * Keep date headers fixed while scrolling.  See FullCalendar docs.
     */
    stickyHeaderDates: PropTypes.bool,
    /**
     * Show sticky scrollbar at the bottom.  See FullCalendar docs.
     */
    stickyFooterScrollbar: PropTypes.bool,
    /**
     * Date the calendar navigates to on first render.  See FullCalendar docs.
     */
    initialDate: PropTypes.oneOfType([PropTypes.string, PropTypes.instanceOf(Date)]),
    /**
     * Restricts navigation/selection to a date range.  See FullCalendar docs.
     */
    validRange: PropTypes.oneOfType([PropTypes.object, PropTypes.func]),
    /**
     * Precisely set the range of dates shown in a custom view.  See FullCalendar docs.
     */
    visibleRange: PropTypes.func,
    /**
     * Date-formatting skeleton or object for the view title.  See FullCalendar docs.
     */
    titleFormat: PropTypes.oneOfType([PropTypes.object, PropTypes.string]),
    /**
     * Calendar locale code (e.g. ‘en-gb’).  See FullCalendar docs.
     */
    locale: PropTypes.string,
    /**
     * Array of additional locale objects to load.  See FullCalendar docs.
     */
    locales: PropTypes.array,
    /**
     * Text direction: ‘ltr’ or ‘rtl’.  See FullCalendar docs.
     */
    dir: PropTypes.string,
    /**
     * Index of week’s first day (0=Sunday).  See FullCalendar docs.
     */
    firstDay: PropTypes.number,
    /**
     * Show weekend columns.  See FullCalendar docs.
     */
    weekends: PropTypes.bool,
    /**
     * Array of day numbers to hide (0=Sun).  See FullCalendar docs.
     */
    hiddenDays: PropTypes.array,
    /**
     * Always render 6 weeks in month view.  See FullCalendar docs.
     */
    fixedWeekCount: PropTypes.bool,
    /**
     * Render leading/trailing days in month view.  See FullCalendar docs.
     */
    showNonCurrentDates: PropTypes.bool,
    /**
     * Collapse rows after this many events per day.  See FullCalendar docs.
     */
    dayMaxEvents: PropTypes.oneOfType([PropTypes.bool, PropTypes.number]),
    /**
     * Alternate way to cap events per day (rows).  See FullCalendar docs.
     */
    dayMaxEventRows: PropTypes.oneOfType([PropTypes.bool, PropTypes.number]),
    /**
     * Minimum pixel width of a day column.  See FullCalendar docs.
     */
    dayMinWidth: PropTypes.number,
    /**
     * Action when a ‘+ more’ link is clicked.  See FullCalendar docs.
     */
    moreLinkClick: PropTypes.oneOfType([PropTypes.string, PropTypes.func]),
    /**
     * Custom renderer for the ‘+ more’ link.  See FullCalendar docs.
     */
    moreLinkContent: PropTypes.oneOfType([PropTypes.func, PropTypes.node]),
    /**
     * Text factory for the ‘+ more’ link.  See FullCalendar docs.
     */
    moreLinkText: PropTypes.oneOfType([PropTypes.string, PropTypes.func]),
    /**
     * Class names for the ‘+ more’ link.  See FullCalendar docs.
     */
    moreLinkClassNames: PropTypes.oneOfType([PropTypes.array, PropTypes.object, PropTypes.string, PropTypes.func]),
    /**
     * Callback after the ‘+ more’ link mounts.  See FullCalendar docs.
     */
    moreLinkDidMount: PropTypes.func,
    /**
     * Callback before the ‘+ more’ link unmounts.  See FullCalendar docs.
     */
    moreLinkWillUnmount: PropTypes.func,
    /**
     * Date-format skeleton for the day popover.  See FullCalendar docs.
     */
    dayPopoverFormat: PropTypes.oneOfType([PropTypes.object, PropTypes.string]),
    /**
     * Show ISO week numbers down the side.  See FullCalendar docs.
     */
    weekNumbers: PropTypes.bool,
    /**
     * Formatter for week-number text.  See FullCalendar docs.
     */
    weekNumberFormat: PropTypes.oneOfType([PropTypes.object, PropTypes.string]),
    /**
     * Custom week-number algorithm.  See FullCalendar docs.
     */
    weekNumberCalculation: PropTypes.oneOfType([PropTypes.string, PropTypes.func]),
    /**
     * Short label preceding week numbers.  See FullCalendar docs.
     */
    weekText: PropTypes.string,
    /**
     * Long label preceding week numbers.  See FullCalendar docs.
     */
    weekTextLong: PropTypes.string,
    /**
     * Business-hours definition(s) or `true` for default.  See FullCalendar docs.
     */
    businessHours: PropTypes.oneOfType([PropTypes.bool, PropTypes.object, PropTypes.array]),
    /**
     * Function/string/Date returning the ‘current’ date.  See FullCalendar docs.
     */
    now: PropTypes.oneOfType([PropTypes.string, PropTypes.instanceOf(Date), PropTypes.func]),
    /**
     * Render a line marking the current time.  See FullCalendar docs.
     */
    nowIndicator: PropTypes.bool,
    /**
     * Initial scroll position of time-grid views.  See FullCalendar docs.
     */
    scrollTime: PropTypes.oneOfType([PropTypes.string, PropTypes.object]),
    /**
     * Reset scroll position when changing views.  See FullCalendar docs.
     */
    scrollTimeReset: PropTypes.bool,
    /**
     * Granularity of the vertical time slots.  See FullCalendar docs.
     */
    slotDuration: PropTypes.oneOfType([PropTypes.string, PropTypes.object]),
    /**
     * Interval between slot labels.  See FullCalendar docs.
     */
    slotLabelInterval: PropTypes.oneOfType([PropTypes.string, PropTypes.object]),
    /**
     * Formatter(s) for slot labels.  See FullCalendar docs.
     */
    slotLabelFormat: PropTypes.oneOfType([PropTypes.array, PropTypes.object, PropTypes.string]),
    /**
     * Earliest time shown on a day.  See FullCalendar docs.
     */
    slotMinTime: PropTypes.oneOfType([PropTypes.string, PropTypes.object]),
    /**
     * Latest time shown on a day.  See FullCalendar docs.
     */
    slotMaxTime: PropTypes.oneOfType([PropTypes.string, PropTypes.object]),
    /**
     * Minimum pixel width of a resource column.  See FullCalendar docs.
     */
    slotMinWidth: PropTypes.number,
    /**
     * Grid snapping interval while dragging.  See FullCalendar docs.
     */
    snapDuration: PropTypes.oneOfType([PropTypes.string, PropTypes.object]),
    /**
     * Display the all-day row in time-grid views.  See FullCalendar docs.
     */
    allDaySlot: PropTypes.bool,
    /**
     * Text label for the all-day slot.  See FullCalendar docs.
     */
    allDayText: PropTypes.string,
    /**
     * Class names for the all-day row.  See FullCalendar docs.
     */
    allDayClassNames: PropTypes.oneOfType([PropTypes.array, PropTypes.object, PropTypes.string, PropTypes.func]),
    /**
     * Custom renderer for the all-day cell.  See FullCalendar docs.
     */
    allDayContent: PropTypes.oneOfType([PropTypes.func, PropTypes.node]),
    /**
     * Callback after the all-day row mounts.  See FullCalendar docs.
     */
    allDayDidMount: PropTypes.func,
    /**
     * Callback before the all-day row unmounts.  See FullCalendar docs.
     */
    allDayWillUnmount: PropTypes.func,
    /**
     * Class names for resource lanes.  See FullCalendar docs.
     */
    slotLaneClassNames: PropTypes.oneOfType([PropTypes.array, PropTypes.object, PropTypes.string, PropTypes.func]),
    /**
     * Custom renderer for resource lanes.  See FullCalendar docs.
     */
    slotLaneContent: PropTypes.oneOfType([PropTypes.func, PropTypes.node]),
    /**
     * Callback after a lane mounts.  See FullCalendar docs.
     */
    slotLaneDidMount: PropTypes.func,
    /**
     * Callback before a lane unmounts.  See FullCalendar docs.
     */
    slotLaneWillUnmount: PropTypes.func,
    /**
     * Class names for slot labels.  See FullCalendar docs.
     */
    slotLabelClassNames: PropTypes.oneOfType([PropTypes.array, PropTypes.object, PropTypes.string, PropTypes.func]),
    /**
     * Custom renderer for slot labels.  See FullCalendar docs.
     */
    slotLabelContent: PropTypes.oneOfType([PropTypes.func, PropTypes.node]),
    /**
     * Callback after a slot label mounts.  See FullCalendar docs.
     */
    slotLabelDidMount: PropTypes.func,
    /**
     * Callback before a slot label unmounts.  See FullCalendar docs.
     */
    slotLabelWillUnmount: PropTypes.func,
    /**
     * Formatter for day-header text.  See FullCalendar docs.
     */
    dayHeaderFormat: PropTypes.oneOfType([PropTypes.object, PropTypes.string]),
    /**
     * Class names for day headers.  See FullCalendar docs.
     */
    dayHeaderClassNames: PropTypes.oneOfType([PropTypes.array, PropTypes.object, PropTypes.string, PropTypes.func]),
    /**
     * Custom renderer for day headers.  See FullCalendar docs.
     */
    dayHeaderContent: PropTypes.oneOfType([PropTypes.func, PropTypes.node]),
    /**
     * Callback after a day header mounts.  See FullCalendar docs.
     */
    dayHeaderDidMount: PropTypes.func,
    /**
     * Callback before a day header unmounts.  See FullCalendar docs.
     */
    dayHeaderWillUnmount: PropTypes.func,
    /**
     * Class names for day cells.  See FullCalendar docs.
     */
    dayCellClassNames: PropTypes.oneOfType([PropTypes.array, PropTypes.object, PropTypes.string, PropTypes.func]),
    /**
     * Custom renderer for day cells.  See FullCalendar docs.
     */
    dayCellContent: PropTypes.oneOfType([PropTypes.func, PropTypes.node]),
    /**
     * Callback after a day cell mounts.  See FullCalendar docs.
     */
    dayCellDidMount: PropTypes.func,
    /**
     * Callback before a day cell unmounts.  See FullCalendar docs.
     */
    dayCellWillUnmount: PropTypes.func,
    /**
     * Formatter for list view group headers.  See FullCalendar docs.
     */
    listDayFormat: PropTypes.oneOfType([PropTypes.object, PropTypes.string, PropTypes.bool]),
    /**
     * Formatter for list view side headers.  See FullCalendar docs.
     */
    listDaySideFormat: PropTypes.oneOfType([PropTypes.object, PropTypes.string, PropTypes.bool]),
    /**
     * Class names applied when no events are present.  See FullCalendar docs.
     */
    noEventsClassNames: PropTypes.oneOfType([PropTypes.array, PropTypes.object, PropTypes.string, PropTypes.func]),
    /**
     * Custom ‘no events’ content renderer.  See FullCalendar docs.
     */
    noEventsContent: PropTypes.oneOfType([PropTypes.func, PropTypes.node]),
    /**
     * Callback after ‘no events’ content mounts.  See FullCalendar docs.
     */
    noEventsDidMount: PropTypes.func,
    /**
     * Callback before ‘no events’ content unmounts.  See FullCalendar docs.
     */
    noEventsWillUnmount: PropTypes.func,
    /**
     * Enable day/week navigation links.  See FullCalendar docs.
     */
    navLinks: PropTypes.bool,
    /**
     * Handler for day navigation link clicks.  See FullCalendar docs.
     */
    navLinkDayClick: PropTypes.oneOfType([PropTypes.func, PropTypes.string]),
    /**
     * Handler for week navigation link clicks.  See FullCalendar docs.
     */
    navLinkWeekClick: PropTypes.oneOfType([PropTypes.func, PropTypes.string]),
    /**
     * Tooltip for navigation links.  See FullCalendar docs.
     */
    navLinkHint: PropTypes.oneOfType([PropTypes.string, PropTypes.func]),
    /**
     * Max columns in multi-month view.  See FullCalendar docs.
     */
    multiMonthMaxColumns: PropTypes.number,
    /**
     * Min width for multi-month columns.  See FullCalendar docs.
     */
    multiMonthMinWidth: PropTypes.number,
    /**
     * Title format for multi-month view.  See FullCalendar docs.
     */
    multiMonthTitleFormat: PropTypes.oneOfType([PropTypes.object, PropTypes.string]),
    /**
     * Custom view definitions mapped by name.  See FullCalendar docs.
     */
    views: PropTypes.object,
    /**
     * Additional plugins. Accepts plugin instances (objects/functions) and/or plugin names (strings).
     * If strings match Premium plugins (e.g., 'scrollgrid', 'resourceTimeline', 'resourceTimeGrid', 'resource'),
     * they will be lazy-loaded only when `schedulerLicenseKey` is provided. Unknown strings are ignored.
     */
    plugins: PropTypes.arrayOf(PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object,
        PropTypes.func
    ])),
    /**
     * FullCalendar Premium (Scheduler) license key. Required when using any Premium plugin
     * such as resource views or scrollgrid. See docs: https://fullcalendar.io/docs/schedulerLicenseKey
     */
    schedulerLicenseKey: PropTypes.string,
    /**
     * Array of event source objects.  See FullCalendar docs.
     */
    eventSources: PropTypes.array,
    /**
     * Default all-day status for new events.  See FullCalendar docs.
     */
    defaultAllDay: PropTypes.bool,
    /**
     * Formatter for event time text.  See FullCalendar docs.
     */
    eventTimeFormat: PropTypes.oneOfType([PropTypes.object, PropTypes.string]),
    /**
     * Show event time.  See FullCalendar docs.
     */
    displayEventTime: PropTypes.bool,
    /**
     * Show event end time.  See FullCalendar docs.
     */
    displayEventEnd: PropTypes.bool,
    /**
     * Threshold for "next day" calculation.  See FullCalendar docs.
     */
    nextDayThreshold: PropTypes.oneOfType([PropTypes.string, PropTypes.object]),
    /**
     * Rendering style for events.  See FullCalendar docs.
     */
    eventDisplay: PropTypes.string,
    /**
     * Default background color for events.  See FullCalendar docs.
     */
    eventBackgroundColor: PropTypes.string,
    /**
     * Default border color for events.  See FullCalendar docs.
     */
    eventBorderColor: PropTypes.string,
    /**
     * Default text color for events.  See FullCalendar docs.
     */
    eventTextColor: PropTypes.string,
    /**
     * Default color for events.  See FullCalendar docs.
     */
    eventColor: PropTypes.string,
    /**
     * Determines event sort order.  See FullCalendar docs.
     */
    eventOrder: PropTypes.oneOfType([PropTypes.array, PropTypes.string, PropTypes.func]),
    /**
     * Enforce strict event ordering.  See FullCalendar docs.
     */
    eventOrderStrict: PropTypes.bool,
    /**
     * Class names for events.  See FullCalendar docs.
     */
    eventClassNames: PropTypes.oneOfType([PropTypes.array, PropTypes.object, PropTypes.string, PropTypes.func]),
    /**
     * Custom renderer for events.  See FullCalendar docs.
     */
    eventContent: PropTypes.oneOfType([PropTypes.func, PropTypes.node]),
    /**
     * Callback after an event is mounted.  See FullCalendar docs.
     */
    eventDidMount: PropTypes.func,
    /**
     * Callback before an event is unmounted.  See FullCalendar docs.
     */
    eventWillUnmount: PropTypes.func,
    /**
     * Transform event data before rendering.  See FullCalendar docs.
     */
    eventDataTransform: PropTypes.func,
    /**
     * Name of start date GET param.  See FullCalendar docs.
     */
    startParam: PropTypes.string,
    /**
     * Name of end date GET param.  See FullCalendar docs.
     */
    endParam: PropTypes.string,
    /**
     * Name of time zone GET param.  See FullCalendar docs.
     */
    timeZoneParam: PropTypes.string,
    /**
     * Fetch events only when needed.  See FullCalendar docs.
     */
    lazyFetching: PropTypes.bool,
    /**
     * Render events as they load.  See FullCalendar docs.
     */
    progressiveEventRendering: PropTypes.bool,
    /**
     * Delay before rerendering events.  See FullCalendar docs.
     */
    rerenderDelay: PropTypes.number,
    /**
     * Callback for loading state.  See FullCalendar docs.
     */
    loading: PropTypes.func,
    /**
     * Allow events to be editable.  See FullCalendar docs.
     */
    editable: PropTypes.bool,
    /**
     * Allow event start to be editable.  See FullCalendar docs.
     */
    eventStartEditable: PropTypes.bool,
    /**
     * Allow resizing events from start.  See FullCalendar docs.
     */
    eventResizableFromStart: PropTypes.bool,
    /**
     * Allow event duration to be editable.  See FullCalendar docs.
     */
    eventDurationEditable: PropTypes.bool,
    /**
     * Duration for drag revert animation.  See FullCalendar docs.
     */
    dragRevertDuration: PropTypes.number,
    /**
     * Allow calendar to scroll during drag.  See FullCalendar docs.
     */
    dragScroll: PropTypes.bool,
    /**
     * Allow external elements to be dropped.  See FullCalendar docs.
     */
    droppable: PropTypes.bool,
    /**
     * Selector or function to accept drops.  See FullCalendar docs.
     */
    dropAccept: PropTypes.oneOfType([PropTypes.string, PropTypes.func]),
    /**
     * Allow events to overlap.  See FullCalendar docs.
     */
    eventOverlap: PropTypes.oneOfType([PropTypes.bool, PropTypes.func]),
    /**
     * Event constraint for dragging/resizing.  See FullCalendar docs.
     */
    eventConstraint: PropTypes.oneOfType([PropTypes.object, PropTypes.string]),
    /**
     * Determines if an event can be moved/resized.  See FullCalendar docs.
     */
    eventAllow: PropTypes.func,
    /**
     * Allow date/time range selection.  See FullCalendar docs.
     */
    selectable: PropTypes.bool,
    /**
     * Show a mirror of selection while dragging.  See FullCalendar docs.
     */
    selectMirror: PropTypes.bool,
    /**
     * Unselect when clicking outside.  See FullCalendar docs.
     */
    unselectAuto: PropTypes.bool,
    /**
     * CSS selector for elements that prevent unselect.  See FullCalendar docs.
     */
    unselectCancel: PropTypes.string,
    /**
     * Allow selection to overlap events.  See FullCalendar docs.
     */
    selectOverlap: PropTypes.oneOfType([PropTypes.bool, PropTypes.func]),
    /**
     * Selection constraint for selecting.  See FullCalendar docs.
     */
    selectConstraint: PropTypes.oneOfType([PropTypes.object, PropTypes.string]),
    /**
     * Determines if a selection is allowed.  See FullCalendar docs.
     */
    selectAllow: PropTypes.func,
    /**
     * Minimum drag distance before selection.  See FullCalendar docs.
     */
    selectMinDistance: PropTypes.number,
    /**
     * Delay for long press (ms).  See FullCalendar docs.
     */
    longPressDelay: PropTypes.number,
    /**
     * Delay for event long press (ms).  See FullCalendar docs.
     */
    eventLongPressDelay: PropTypes.number,
    /**
     * Delay for select long press (ms).  See FullCalendar docs.
     */
    selectLongPressDelay: PropTypes.number,
    /**
     * Class names for the view container.  See FullCalendar docs.
     */
    viewClassNames: PropTypes.oneOfType([PropTypes.array, PropTypes.object, PropTypes.string, PropTypes.func]),
    /**
     * Callback after a view is mounted.  See FullCalendar docs.
     */
    viewDidMount: PropTypes.func,
    /**
     * Callback before a view is unmounted.  See FullCalendar docs.
     */
    viewWillUnmount: PropTypes.func,
    /**
     * Mouse enters event.  See FullCalendar docs.
     */
    eventMouseEnter: PropTypes.func,
    /**
     * Mouse leaves event.  See FullCalendar docs.
     */
    eventMouseLeave: PropTypes.func,
    /**
     * Event drag starts.  See FullCalendar docs.
     */
    eventDragStart: PropTypes.func,
    /**
     * Event drag stops.  See FullCalendar docs.
     */
    eventDragStop: PropTypes.func,
    /**
     * Event resize starts.  See FullCalendar docs.
     */
    eventResizeStart: PropTypes.func,
    /**
     * Event resize stops.  See FullCalendar docs.
     */
    eventResizeStop: PropTypes.func,
    /**
     * Callback for drop of external elements.  See FullCalendar docs.
     */
    drop: PropTypes.func,
    /**
     * Callback when an external event is received.  See FullCalendar docs.
     */
    eventReceive: PropTypes.func,
    /**
     * Callback when an external event is removed.  See FullCalendar docs.
     */
    eventLeave: PropTypes.func,

    /**
     * An object specifying a command to execute on the calendar API, such as {'type': 'next'} to navigate to the next period.
     */
    command: PropTypes.object,

    /* Dash glue - output props for callbacks */
    /**
     * The date string of the clicked date, for use in Dash callbacks.
     */
    dateClick: PropTypes.any,
    /**
     * Object containing the selected range information, for use in Dash callbacks.
     */
    select: PropTypes.any,
    /**
     * Flag indicating unselection occurred, for use in Dash callbacks.
     */
    unselect: PropTypes.any,
    /**
     * Object containing information about the clicked event, for use in Dash callbacks.
     */
    eventClick: PropTypes.any,
    /**
     * Object containing information about the dropped event, for use in Dash callbacks.
     */
    eventDrop: PropTypes.any,
    /**
     * Object containing information about the resized event, for use in Dash callbacks.
     */
    eventResize: PropTypes.any,
    /**
     * Object containing information about the added event, for use in Dash callbacks.
     */
    eventAdd: PropTypes.any,
    /**
     * Object containing information about the changed event, for use in Dash callbacks.
     */
    eventChange: PropTypes.any,
    /**
     * Object containing information about the removed event, for use in Dash callbacks.
     */
    eventRemove: PropTypes.any,
    /**
     * Object containing the current date range, for use in Dash callbacks.
     */
    datesSet: PropTypes.any,
    /**
     * Array of current event objects in the calendar, for use in Dash callbacks.
     */
    eventsSet: PropTypes.any,
    /**
     * Dash-assigned callback that should be called to report property changes to Dash, registered automatically.
     */
    setProps: PropTypes.func
};

export default DashFullCalendar;