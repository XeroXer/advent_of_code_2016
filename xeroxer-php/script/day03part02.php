<?php
chdir(dirname(__DIR__));
if (!is_file('input/day03')) {
    throw new Exception('Input file for day not found');
}
$input = new SplFileObject('input/day03');
$input->setFlags(SplFileObject::READ_AHEAD | SplFileObject::SKIP_EMPTY);

$possibleTriangles = 0;
$columnData = [];

while (!$input->eof()) {
    $line = preg_replace('/\s+/', ' ', trim($input->current()));
    $input->next();

    $columnData[] = array_map('intval', explode(' ', $line));

    if (count($columnData) == 3) {
        for ($i = 0; $i < 3; ++$i) {
            if (($columnData[0][$i] + $columnData[1][$i]) > $columnData[2][$i]
                && ($columnData[0][$i] + $columnData[2][$i]) > $columnData[1][$i]
                && ($columnData[2][$i] + $columnData[1][$i]) > $columnData[0][$i]
            ) {
                ++$possibleTriangles;
            }
        }

        $columnData = [];
    }
}

echo $possibleTriangles . ' of the listed triangles are possible' . PHP_EOL;
