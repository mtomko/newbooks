<?php 
include_once('months.php');

$prev_months = get_prev_months(4);

function normalize_class($class) {
	return preg_replace('/[^A-Za-z]/', '', $class);
}

// get the book class form parameter
if (isset($_GET['c'])) {
  $display_book_class = $_GET['c'];
} else {
  $display_book_class = 'Diversions';
}

$file_book_class = normalize_class($display_book_class);

// get the book month form parameter
if (isset($_GET['m'])) {
  $book_month = $_GET['m'];
} else {
  $book_month = date('F',mktime (0,0,0,date("m")-1,date("d"), date("Y")));
}

// get the page number form parameter
if (isset($_GET['p'])) {
	$page_number = $_GET['p'];
} else {
	$page_number = 1;
}

?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Simmons College Library</title>
<base target="_self" />
<link rel="stylesheet" type="text/css" href="/scripts/ProStyles.css" />
<link rel="stylesheet" type="text/css" href="/screens/styles.css" media="screen and (min-device-width: 481px)" />
<link rel="shortcut icon" type="ximage/icon" href="/screens/favicon.ico" />

<script language="JavaScript" type="text/javascript" src="/scripts/common.js"></script>
<script language="JavaScript" type="text/javascript" src="/scripts/elcontent.js"></script>
<script src="/screens/js_includes/scriptaculous/prototype.js" type="text/javascript"></script>
<script src="/screens/js_includes/scriptaculous/scriptaculous.js" type="text/javascript"></script>
<script type="text/javascript" src="/screens/bibdisplay.js"></script>
<script type="text/javascript" src="/screens/brief.js"></script>
<script language="javascript" src="http://libfs2.simmons.edu/opac/refworks/add_to_refworks.js" type="text/javascript"></script>

<link rel="stylesheet" type="text/css" media="screen" href="http://www.simmons.edu/c/generalLayout-fall08/resetNew.css" />
<link rel="stylesheet" type="text/css" media="screen" href="http://www.simmons.edu/j/jquery/thickbox/thickbox.css" />
<link rel="stylesheet" type="text/css" media="screen" href="http://www.simmons.edu/frances/xsitenav/c/xsitenav.css" />
<link rel="stylesheet" type="text/css" media="screen" href="http://www.simmons.edu/library/c/screen.css" />
<link rel="stylesheet" type="text/css" href="/screens/styles.css" title="default" />
<link rel="stylesheet" type="text/css" href="/screens/styles.css">
<link rel="stylesheet" type="text/css" href="http://library.simmons.edu:2082/screens/styles.css" />
<link rel="stylesheet" type="text/css" href="http://libfs2.simmons.edu/sandbox/majax-style.css" />

<!-- IE specific CSS  -->
<!--[if lte IE 8]><link rel="stylesheet" type="text/css" href="/screens/ie_styles.css" /><![endif]-->
<!--[if IE 7]><link rel="stylesheet" type="text/css" media="screen" href="http://www.simmons.edu/library/c/ie7.css" /><![endif]-->
<!--[if lt IE 7]><link rel="stylesheet" type="text/css" media="screen" href="http://www.simmons.edu/library/c/ie.css" /><![endif]-->

<script type="text/javascript" src="http://library.simmons.edu/screens/majax.js"></script>
<script src="http://library.simmons.edu/screens/gbsclasses.js" type="text/javascript"></script>
<script src="http://libx.org/gbs/gbsclasses.js" type="text/javascript"></script>
</head>

<body id="library" class="lvl2 library home sIFR-active">
  <script language="javascript" src="http://libfs2.simmons.edu/opac/refworks/add_to_refworks.js" type="text/javascript"></script>

  <script type="text/javascript">
    /* <![CDATA[ */
    function load() {
        get_recordnum();
		startList();
		if (location.search.indexOf('SUBKEY') != -1 || location.search.indexOf('SEARCH') != -1 || location.search.indexOf('searcharg=') != -1)
		    modifySearch(document.location.search);
		init_progsearch();
		if (document.search)
			document.search.searchText1.focus();
	}

	window.onload = load;
	/* <![CDATA[ */
  </script>

  <div id="container">
    <div id="headerWrapper">
      <div id="xsitenav">

        <ul>

          <li id="home-xnav"><a href="http://www.simmons.edu/">Simmons Home</a></li>
          <li id="school-xnav"><a href="http://www.simmons.edu/overview/academics/schools/">Schools</a>
            <div id="school-drop">
              <ul class="subnav">
                <li id="xsite-ug"><a href="http://www.simmons.edu/undergraduate/">Undergraduate College of Arts and Sciences</a></li>
                <li id="xsite-casgs"><a href="http://www.simmons.edu/graduate/">College of Arts and Sciences Graduate Studies</a></li>
                <li id="xsite-gslis"><a href="http://www.simmons.edu/gslis/">Graduate School of Library and Information Science</a></li>
                <li id="xsite-shs"><a href="http://www.simmons.edu/shs/">Graduate School of Health Sciences</a></li>
                <li id="xsite-som"><a href="http://www.simmons.edu/som/">Graduate School of Management</a></li>
                <li id="xsite-ssw"><a href="http://www.simmons.edu/ssw/">Graduate School of Social Work</a></li>
              </ul>
            </div> <!-- school-drop --></li>
          <li id="programs-xnav"><a href="http://www.simmons.edu/overview/academics/programs/">All Programs</a>
            <div id="programs-drop">
              <p>
                With over 40 undergraduate majors and five graduate schools, Simmons offers too many programs to list here. <a href="http://www.simmons.edu/overview/academics/programs/">Check them all out &raquo;</a>
              </p>
            </div> <!-- programs-drop --></li>

          <li id="sites-xnav"><a href="http://www.simmons.edu/index/websites/">Our Websites</a>

            <div id="sites-drop">

              <div class="col col1">

                <h3>Admissions</h3>
                <ul class="subnav">
                  <li><a href="http://www.simmons.edu/overview/admission/">Main Website</a></li>
                  <li><a href="http://www.simmons.edu/undergraduate/admission/">Undergraduate College</a></li>

                  <li><a href="http://www.simmons.edu/gradstudies/admission/">CAS Graduate Study</a></li>

                  <li><a href="http://www.simmons.edu/gslis/admission/">Library and Information Science</a></li>
                  <li><a href="http://www.simmons.edu/shs/admission/">Health Sciences</a></li>
                  <li><a href="http://www.simmons.edu/som/mba/admission/">Management</a></li>
                  <li><a href="http://www.simmons.edu/ssw/admission/">Social Work</a></li>
                </ul>

                <h3>Online Communities</h3>
                <ul class="subnav">
                  <li><a href="http://alumnet.simmons.edu/">Alumnet</a></li>
                  <li><a href="http://my.simmons.edu/">MySimmons Intranet</a></li>
                </ul>
              </div>
              <!-- col col1 -->
              <!-- close col1 -->

              <div class="col col2">
                <h3>Microsites</h3>
                <ul class="subnav">
                  <li><a href="http://www.simmons.edu/athletics/">Athletics</a></li>
                  <li><a href="http://www.simmons.edu/financialaid/">Financial Aid</a></li>
                  <li><a href="http://www.simmons.edu/commencement/">Commencement</a></li>
                  <li><a href="http://www.simmons.edu/orientation/">Orientation</a></li>
                  <li><a href="http://www.simmons.edu/leadership/">Leadership Conference</a></li>
                  <li><a href="http://green.simmons.edu/">Green Simmons</a></li>
                  <li><a href="http://itunes.simmons.edu/">iTunes U</a></li>
                </ul>

                <h3>Online Services</h3>
                <ul class="subnav">
                  <li><a href="http://aarc.simmons.edu/">AARC</a></li>
                  <li><a href="http://elearning.simmons.edu/">eLearning</a></li>
                  <li><a href="http://email.simmons.edu/">WebMail</a></li>
                  <li><a href="https://portal.simmons.edu/services/">more...</a></li>
                </ul>
              </div>
              <!-- close col2 -->

              <div class="col col3">
                <h3>On the Web</h3>
                <ul class="subnav">
                  <li><a href="http://www.facebook.com/simmonscollege">Facebook</a></li>
                  <li><a href="http://twitter.com/SimmonsCollege">Twitter</a></li>
                  <li><a href="http://www.youtube.com/user/simmonscollege">YouTube</a></li>
                  <li><a href="http://www.linkedin.com/groups?gid=133279">LinkedIn</a></li>
                </ul>
              </div>
              <!-- close col3 -->

            </div>
            <!-- sites-drop --></li>
        </ul>

      </div>
      <!-- xsitenav -->
      <!-- close xsite nav -->
      <div id="header" class="vcard">

        <!-- Begin Microformats hCard -->
        <h1 class="org">
          <a class="url fn" href="http://www.simmons.edu">Simmons College</a>
        </h1>

        <p class="adr hidden">
          <span class="street-address">300 The Fenway</span><br /> <span class="locality">Boston</span>, <span class="region">MA</span> <span class="postal-code">02115</span><br /> <span class="tel hidden">617-521-2000</span>
        </p>
        <!-- End Microformats hCard -->

        <div class="search">
          <!-- Search Google -->
          <form method="get" action="http://search.simmons.edu/search">
            <p style="margin: 0;">
              <input type="search" placeholder="Search Simmons" results="5" id="q" name="q" maxlength="256" value="" />
              <button class="searchButton" type="submit">Search</button>

              <!--<input type="submit" id="btnG" name="btnG" value="Search" />-->
            </p>

            <div class="hidden">
              <input type="hidden" name="site" value="all_simmons" /> <input type="hidden" name="client" value="default_frontend" /> <input type="hidden" name="proxystylesheet" value="all-search" /> <input type="hidden" name="output" value="xml_no_dtd" />
            </div>
          </form>
          <!-- Search Google -->
        </div>
        <!-- close search -->

        <div class="toptools">
          <h3 class="hidden">Site Tools:</h3>
          <ul class="tools ">
            <li><a href="http://www.simmons.edu/index/">Site A-Z</a></li>
            <li><a href="http://www.simmons.edu/overview/offices/people/">Directories</a></li>
            <li class="last"><a href="http://www.simmons.edu/overview/about/contact/">Contact Us</a></li>
          </ul>
        </div>
        <!-- close toptools -->

      </div>
      <!-- close header -->
    </div>
    <!-- close headerWrapper -->


    <div id="navigationContainer">
      <div id="primaryNavigation">
        <h2 class="hidden">Primary Navigation</h2>
        <ul>
          <li id="home-nav" class=""><a href="http://www.simmons.edu/library/index.php">Home</a></li>

          <li id="services-nav"><a href="http://www.simmons.edu/library/services/index.php">Services</a>
            <ul class="subnav">
              <li id="page49"><a class="p49" href="http://www.simmons.edu/library/services/items/index.php">Finding and Borrowing Items</a>
                <ul class="subnav" id="sub49">

                  <li id="page62"><a href="http://www.simmons.edu/library/services/items/marterials.php">Borrowing Materials</a></li>

                  <li id="page61"><a href="http://www.simmons.edu/library/services/items/reserves.php">Borrowing Course Reserves</a></li>

                  <li id="page60"><a href="http://www.simmons.edu/library/services/items/renewing.php">Returning &amp; Renewing Materials</a>
                  </li>
                </ul>
              </li>

              <li id="page48"><a class="p48" href="http://www.simmons.edu/library/services/studying/index.php">Studying in the Library</a>

                <ul class="subnav" id="sub48">
                  <li id="page59"><a href="http://www.simmons.edu/library/services/studying/study-rooms.php">Group Study Rooms</a>
                  </li>

                  <li id="page58"><a href="http://www.simmons.edu/library/services/studying/information-commons.php">Using the Information Commons</a>
                  </li>

                  <li id="page57"><a href="http://www.simmons.edu/library/services/studying/equipment.php">Printers, Copiers, and Scanners</a>
                  </li>

                  <li id="page56"><a href="http://www.simmons.edu/library/services/studying/more.php">Checking Out Laptops, Headphones, and More</a>
                  </li>
                </ul>
              </li>

              <li id="page50"><a class="p50" href="http://www.simmons.edu/library/services/disabilities/index.php">Services for Patrons with Disabilities</a>
              </li>

              <li id="page55"><a class="p55" href="http://www.simmons.edu/library/services/faculty-staff/index.php">Services for Faculty &amp; Staff</a>

                <ul class="subnav" id="sub55">
                  <li id="page76"><a href="http://www.simmons.edu/library/services/faculty-staff/reserves/index.php"> Setting up Course Reserves</a>
                    <ul class="l4">
                      <li id="page77"><a class="p77" href="http://www.simmons.edu/library/services/faculty-staff/reserves/form.php"> Placing Materials on Course Reserve</a>
                      </li>
                    </ul>
                  </li>

                  <li id="page75"><a href="http://www.simmons.edu/library/services/faculty-staff/media.php">Booking Media for Classroom Use</a>
                  </li>

                  <li id="page73"><a href="http://www.simmons.edu/library/services/faculty-staff/scheduling.php">Scheduling A Library Instruction Session</a>
                  </li>

                  <li id="page71"><a href="http://www.simmons.edu/library/services/faculty-staff/research-support.php"> Research Support Services</a>
                  </li>

                  <li id="page364"><a href="http://www.simmons.edu/library/services/faculty-staff/passes.php">Museum Passes</a>
                  </li>
                </ul>
              </li>

              <li id="page52"><a class="p52" href="http://www.simmons.edu/library/services/alumni/index.php">Alumni Services</a></li>

              <li id="page51"><a class="p51" href="http://www.simmons.edu/library/services/flc/index.php">FLC Members &amp; Guest Services</a></li>

              <li id="page47"><a class="p47" href="http://www.simmons.edu/library/services/purchase/index.php">Request a Purchase</a></li>

              <li id="page362"><a class="p362" href="http://www.simmons.edu/library/services/passes/index.php">Museum Passes</a></li>
            </ul></li>

          <li id="research-nav"><a href="http://www.simmons.edu/library/resources/index.php">Research &amp; Resources</a>

            <ul class="subnav">

              <li id="page211"><a class="p49" href="http://www.simmons.edu/library/resources/applied-sciences.php">Applied Sciences</a>
              </li>

              <li id="page210"><a class="p49" href="http://www.simmons.edu/library/resources/arts-humanities.php">Arts &amp; Humanities</a>
              </li>

              <li id="page209"><a class="p49" href="http://www.simmons.edu/library/resources/business-management.php">Business &amp; Management</a>
              </li>

              <li id="page208"><a class="p49" href="http://www.simmons.edu/library/resources/career-resources.php">Career Resources</a>
              </li>

              <li id="page207"><a class="p49" href="http://www.simmons.edu/library/resources/education.php">Education</a>
              </li>

              <li id="page206"><a class="p49" href="http://www.simmons.edu/library/resources/first-year.php">First Year</a>
              </li>

              <li id="page205"><a class="p49" href="http://www.simmons.edu/library/resources/health-sciences.php">Health Sciences</a>
              </li>

              <li id="page204"><a class="p49" href="http://www.simmons.edu/library/resources/lis.php">Library &amp; Information Science</a>
              </li>

              <li id="page203"><a class="p49" href="http://www.simmons.edu/library/resources/social-sciences.php">Social Sciences</a>
              </li>

              <li id="page202"><a class="p49" href="http://www.simmons.edu/library/resources/social-work.php">Social Work</a>
              </li>

            </ul></li>

          <li id="help-nav"><a href="http://www.simmons.edu/library/ask/index.php">Ask a Librarian</a>

            <ul class="subnav">
              <li id="page255"><a class="p49" href="http://www.simmons.edu/library/ask/appointment-request.php">Research Appointment Request</a>
              </li>

              <li id="page25"><a class="p49" href="http://www.simmons.edu/library/ask/workshops.php">Workshops</a>
              </li>
            </ul></li>

          <li id="about-nav"><a href="http://www.simmons.edu/library/about/index.php">About the Library</a>

            <ul class="subnav">
              <li id="page23"><a class="p23" href="http://www.simmons.edu/library/about/hours/index.php">Hours</a>
              </li>

              <li id="page22"><a class="p22" href="http://www.simmons.edu/library/about/staff/index.php">Staff</a>
              </li>

              <li id="page192"><a class="p192" href="http://www.simmons.edu/library/about/mission-vision/index.php">Mission &amp; Vision</a>
              </li>

              <li id="page21"><a class="p21" href="http://www.simmons.edu/library/about/gift/index.php">Make a Gift</a>
              </li>

              <li id="page15"><a href="http://www.simmons.eduhttp://www.simmons.edu/library/blog/" class="p15">News</a>
              </li>

              <li id="page24"><a class="p24" href="http://www.simmons.edu/library/about/maps/index.php">Maps &amp; Directions</a>
              </li>

              <li id="page28"><a class="p28" href="http://www.simmons.edu/library/about/displays/index.php">Displays</a>
              </li>

              <li id="page26"><a class="p26" href="http://www.simmons.edu/library/about/exhibits/index.php">Exhibits</a>
              </li>

              <li id="page340"><a class="p340" href="http://www.simmons.edu/library/about/policies.php">Policies</a>
              </li>

              <li id="page336"><a class="p336" href="http://www.simmons.edu/library/about/jobs.php">Jobs at the Library</a>
              </li>

              <li id="page157"><a class="p157" href="http://www.simmons.edu/library/about/contact.php">Contact Us</a>
              </li>
            </ul></li>
        </ul>
      </div>
      <!-- close primaryNavigation -->
    </div>
    <!-- close navigationContainer -->



    <div id="containerInternal">

      <div id="content">
        <div id="navSection">
          <ul>
            <li id="page12"><a class="p12" href="http://library.simmons.edu/search">Search the Catalog</a>

              <ul class="subnav" id="sub49">
                <li id="page62"><a href="http://library.simmons.edu/">Basic Search</a>
                </li>

                <li id="page62"><a href="http://library.simmons.edu/search/X">Advanced Search</a>
                </li>

                <li id="page61"><a href="http://library.simmons.edu/search/j">Journal Search</a>
                </li>

                <li id="page60"><a href="http://library.simmons.edu/search/v">VHS &amp; DVD Search</a>
                </li>
              </ul></li>
            <li id="page48"><a class="p48" href="http://libfs2.simmons.edu/sandbox/newbooks.html">New Books</a>
              <ul class="subnav" id="sub49">
                <li id="page62"><a href="newbooks.php?c=Applied&nbsp;Sciences">Applied Sciences</a></li>
                <li id="page62"><a href="newbooks.php?c=Arts+%26+Humanities">Arts &amp; Humanities</a></li>
                <li id="page62"><a href="newbooks.php?c=Career">Career</a></li>
   
                <li id="page62"><a href="newbooks.php?c=Diversions">Diversions</a></li>
                <li id="page62"><a href="newbooks.php?c=Education">Education</a></li>
                <li id="page62"><a href="newbooks.php?c=Health+Sciences">Health Sciences</a></li>
                <li id="page62"><a href="newbooks.php?c=Library+Science">Library Science</a></li>
                <li id="page62"><a href="newbooks.php?c=Management">Management</a></li>
                <li id="page62"><a href="newbooks.php?c=Social+Sciences">Social Sciences</a></li>
              </ul></li>
            <li id="page49"><a class="p49" href="http://library.simmons.edu/patroninfo">Login to Catalog</a></li>
            <li id="page50"><a class="p50" href="http://libfs2.simmons.edu/studyrooms">Group Study Rooms</a></li>
            <li id="page51"><a class="p51" href="http://libfs3.simmons.edu/ares">Course Reserves</a>
            </li>
            <li id="page52"><a class="p52" href="http://libfs1.simmons.edu/illiad">Interlibrary Loan</a></li>
            <li id="page53"><a class="p53" href="http://libfs2.simmons.eduhttp://www.simmons.edu/libraryguides">Library Guides</a></li>

          </ul>

        </div>

        <div id="contentA" class="column">
          <div id="pageInformation"></div>
          <h2>New <?=$display_book_class?> Books</h2>
          <h3>
            <span style="font-size: 12pt;">
              <?php for($idx = 1; $idx < count($prev_months); $idx++): ?>
                <?php if ($prev_months[$idx] == $book_month): ?>
                <?php echo $book_month; ?>
                <?php else: ?>
                <a href="newbooks.php?c=<?php echo urlencode($display_book_class); ?>&m=<?=$prev_months[$idx]?>"><?=$prev_months[$idx]?></a>
                <?php endif; ?>
              <?php endfor; ?>
            </span>
          </h3>
          <?php
          	$include_file = "$file_book_class-$book_month-$page_number.php";
          	if (!file_exists($include_file)) {
				echo("Sorry, no new $display_book_class books for this month.");
			} else {
				echo('<p>Click on the cover image for synopsis and reviews.</p>');
          		echo ('<table class="books" border="0" cellpadding="5px">');
				include($include_file);
          	}
          ?>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
