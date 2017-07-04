<?php
chdir(dirname(__DIR__));
if (!is_file('input/day03')) {
    throw new Exception('Input file for day not found');
}
$input = new SplFileObject('input/day03');
$input->setFlags(SplFileObject::READ_AHEAD | SplFileObject::SKIP_EMPTY);

$possibleTriangles = 0;

while (!$input->eof()) {
    $line = preg_replace('/\s+/', ' ', trim($input->current()));
    $input->next();

    list($a, $b, $c) = array_map('intval', explode(' ', $line));
    if (($a + $b) > $c
        && ($a + $c) > $b
        && ($c + $b) > $a
    ) {
        ++$possibleTriangles;
    }
}

echo $possibleTriangles . ' of the listed triangles are possible' . PHP_EOL;
