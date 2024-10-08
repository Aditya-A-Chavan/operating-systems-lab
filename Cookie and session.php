<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {

    session_start();

    $name = $_POST['name'];
    $email = $_POST['email'];
    $age = $_POST['age'];
    $phone = $_POST['phone'];
    $address = $_POST['address'];
    $gender = $_POST['gender'];
    $city = $_POST['city'];

    $errors = [];

    if (empty($name) || empty($email) || empty($age) || empty($phone) || empty($address) || empty($gender) || empty($city)) {
        $errors[] = "All fields are required";
    }

    if (!preg_match("/^[0-9]{10}$/", $phone)) {
        $errors[] = "Phone number must be 10 digits";
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = "Invalid email address";
    }

    if (empty($errors)) {
        echo "Form submitted successfully! Data received: <br>";
        echo "Name: " . $name . "<br>";
        echo "Email: " . $email . "<br>";
        echo "Age: " . $age . "<br>";
        echo "Phone: " . $phone . "<br>";
        echo "Address: " . $address . "<br>";
        echo "Gender: " . $gender . "<br>";
        echo "City: " . $city . "<br>";
    } else {
        echo "Validation errors: <br>";
        foreach ($errors as $error) {
            echo $error . "<br>";
        }
    }

    $_SESSION['name'] = $_POST['name'];
    $_SESSION['email'] = $_POST['email'];

    setcookie('name', $name, time() + (86400 * 30), '/');

    if (isset($_COOKIE['name'])) {
        echo "Cookie value: " . $_COOKIE['name'];
    }

    if (isset($_SESSION['name'])) {
        echo "Session value: " . $_SESSION['name'] . "<br>";
        echo "Session value: " . $_SESSION['email'];
    }
}
?>
    