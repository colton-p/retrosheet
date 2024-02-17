---
layout: d3
title: k-hr
---
hr vs. k
<div id="my_dataviz">
<script type="module">
    import {scatter} from './scatter.js'
    fetch('./k-hr-yr.json')
    .then(function(data) { return data.json(); })
    .then(function(data) { return scatter(data, 'k', 'hr'); })
</script>