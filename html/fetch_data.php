<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

$servername = "localhost";
$username = "schule";
$password = "280188";
$dbname = "tsl2591_data";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT id, time, lux FROM sensor_readings ORDER BY time DESC LIMIT 10";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    echo "<table border='1'>
            <tr>
                <th>ID</th>
                <th>Time</th>
                <th>Lux</th>
            </tr>";
    while($row = $result->fetch_assoc()) {
        echo "<tr>
                <td>" . $row["id"]. "</td>
                <td>" . $row["time"]. "</td>
                <td>" . $row["lux"]. "</td>
              </tr>";
    }
    echo "</table>";
} else {
    echo "0 results";
}
$conn->close();
?>
