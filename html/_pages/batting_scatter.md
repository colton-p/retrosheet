---
layout: d3
title: batting scatter
---
<div id="my_dataviz"></div>

<form id="form">
    <input id="statX" value="h"/>
    <input id="statY" value="hr" />
    <input id="min_pa" value="502" />
    <input id="min_year" value="2000" />
</form>

<script type="module">
    import {scatter} from './scatter.js'
    let allData = [];
    function load() {
        return fetch('./all_lines.json')
        .then(function(d) { return d.json(); })
        .then(function(d) {
            allData = d;
            console.log('loaded:', allData.length);
        });
    }
    function update() {
        const statX = document.getElementById('statX').value;
        const statY = document.getElementById('statY').value;
        const minPa = document.getElementById('min_pa').value;
        const minYear = document.getElementById('min_year').value;
        let data = allData.filter(function(r) { return r.pa >= Number(minPa); })
        data = data.filter(function(r) { return r.year >= Number(minYear); })
        console.log('filtered:', data.length)
        return scatter(data, statX, statY);
    }

    load().then(update);
    Array.from(document.getElementsByTagName('input')).forEach(function(e) { e.onchange = update; });
</script>

