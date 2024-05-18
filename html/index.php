<!DOCTYPE html>
<html>
<head>
    <title>Sensor Readings</title>
    <script>
        function fetchData() {
            var xhr = new XMLHttpRequest();
            xhr.open("GET", "fetch_data.php", true);
            xhr.onreadystatechange = function () {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    document.getElementById("data").innerHTML = xhr.responseText;
                }
            };
            xhr.send();
        }

        setInterval(fetchData, 5000); // Refresh every 5 seconds
        window.onload = fetchData; // Fetch data on page load
    </script>
</head>
<body>
    <h1>Sensor Readings</h1>
    <div id="data">
        <!-- Data will be loaded here -->
    </div>
</body>
</html>
