async function fetchEvents() {
    const res = await fetch('/events');
    const events = await res.json();
    const log = document.getElementById('event-log');
    log.innerHTML = "";
    events.forEach(event => {
        const line = document.createElement('div');
        line.textContent = `${event.timestamp}: ${event.event}`;
        log.appendChild(line);
    });
}

// Fetch new events every 5 seconds
setInterval(fetchEvents, 5000);

// Fetch once immediately
fetchEvents();
