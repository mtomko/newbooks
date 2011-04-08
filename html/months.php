<?php // generates a variable $months

// treats $arr as a circular array and $i as and index
// if $i is between 0 and the length of $arr, returns the $ith element of $arr
// if $i is greater than $arr, then the index "wraps" around to the beginning
// if $i is less than 0, then the indexing is from the end of the list
function circ_idx(array $arr, $i) {
    $len = count($arr);
    $idx = $i % $len;
    if ($idx < 0) {
        return $arr[$len + $idx];   
    }
    return $arr[$idx];
}

// returns an array containing the last $n elements of the array $arr, 
// beginning from $start and counting backwards
function trailing_elements(array $arr, $n, $start) {
    $idx = $n;
    $result = array();
    while($idx > 0) {
        $result[$idx - 1] = circ_idx($arr, $start - $idx--);
    }
    return $result;
}

// contains the names of the months of the year, in order (in English)
$MONTHS = array(
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
);

// returns the name of the current month
function get_month() {
	return $date = gmdate('F');
}

// returns the name of the previous $n months, in descending order
function get_prev_months($n) {
	$MONTHS = array(
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
	);
	$date = gmdate('n');
	return trailing_elements($MONTHS, $n, $date['mon']);
}
