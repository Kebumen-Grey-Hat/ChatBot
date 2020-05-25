<?php
// array multi-dimensi
$array = Array (
    "0" => Array (
        "id" => "ADMIN",
        "name" => "ARJUNA",
        "company" => "PROGRAM"
    ),
    "1" => Array (
        "id" => "USER2",
        "name" => "Bill Gates",
        "company" => "Microsoft"
    ),
    "2" => Array (
        "id" => "USER3",
        "name" => "Mark Zuckerberg",
        "company" => "Facebook"
    )
);

// encode array to json
$json = json_encode(array('data' => $array));

// write json to file
if (file_put_contents("data.json", $json)){
    echo "File JSON sukses dibuat...";
} else {
    echo "Oops! Terjadi error saat membuat file JSON...";
}
?>
