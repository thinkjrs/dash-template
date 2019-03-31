"""
index.py

Defines the index_string variable for the musicfox.io Dash application.
"""
import dash

class MFDash(dash.Dash):
    def interpolate_index(self, **kwargs):
        return """
<!DOCTYPE html>
<html>

<head>
    {metas} 
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>MF</title>
    
    {favicon}
    {css}
    <!-- Bootstrap CSS CDN -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css" integrity="sha384-9gVQ4dYFwwWSjIDZnLEWnxCjeSWFphJiwGPXr1jddIhOegiu1FwO5qRGvFXOdJZ4" crossorigin="anonymous">
    <!-- Our Custom CSS 
    <link rel="stylesheet" href="style4.css">-->
    <!-- fontawesome pro-->
    <link href="assets/fontawesome-pro/css/all.css" rel="stylesheet">
</head>

<body>

    <div class="wrapper">
        <!-- Sidebar  -->
        <nav id="sidebar">
            <div class="sidebar-header">
                <img src="assets/logo-white.png" class="img-responsive"> 
                </img>
                <strong>
                    <i class="fal fa-headphones"></i>
                </strong>
            </div>
            <ul class="list-unstyled components">
                <li class="active">
                    <a href="#dashboard">
                        <i class="fas fa-tachometer-alt"></i>
                        Dashboard
                    </a>
                    <a href="#reportsSubmenu" data-toggle="collapse" aria-expanded="true" class="dropdown-toggle">
                        <i class="fas fa-newspaper"></i>
                       	Reports 
                    </a>
                    <ul class="collapse list-unstyled" id="reportsSubmenu">
                        <li>
                            <a href="#">Weekly</a>
                        </li>
                        <li>
                            <a href="#">Quarterly</a>
                        </li>
                        <li>
                            <a href="#">Yearly</a>
                        </li>
                    </ul>
                </li>
                <li>
                    <a href="#Settings">
                        <i class="fas fa-wrench fa-rotate-270"></i>
                        Settings
                    </a> 
                <li>
                    <a href="#help">
                        <i class="fas fa-paper-plane"></i>
                        Help
                    </a>
                </li>
            </ul>

        </nav>

        <!-- Page Content  -->
        <div id="content">
            <nav class="navbar navbar-expand-lg navbar-light"> 
                <div class="container-fluid", id="navbar-button-container">

                    <button type="button" id="sidebarCollapse" class="btn ">
                        <i class="fas fa-align-left"></i>
                    </button>
                    <form class="form-inline my-2 my-lg-0">
                        <input class="form-control mr-sm-2" type="search" placeholder="Type an artist" aria-label="Search">
                        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
                    </form>
                    <button type="button" id="userButton-navbar" class="btn btn-light">
                        <i class="fas fa-user"></i>
                    </button>
                </div>
            </nav>
            <div id="app-content">
                {app_entry}
            </div>
        </div>
    </div>
    <footer>
        {config}
        {scripts}
        <!-- jQuery CDN - Slim version (=without AJAX) -->
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <!-- Popper.JS -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js" integrity="sha384-cs/chFZiN24E4KMATLdqdvsezGxaGsi4hLGOzlXwp5UZB1LY//20VyM2taTB4QvJ" crossorigin="anonymous"></script>
        <!-- Bootstrap JS -->
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js" integrity="sha384-uefMccjFJAIv6A+rW+L4AHf99KvxDjWSu1z9VI8SKNVmz4sk7buKt/6v9KI65qnm" crossorigin="anonymous"></script>

        <script type="text/javascript">
            $(document).ready(function () {{
                $('#sidebarCollapse').on('click', function () {{
                    $('#sidebar').toggleClass('active');
                    $(this).toggleClass('active');
                }});
            }});
        </script>
        {renderer}
    </footer>
</body>

</html>""".format(
            metas=kwargs["metas"],
            favicon=kwargs["favicon"],
            css=kwargs["css"],
            app_entry=kwargs["app_entry"],
            config=kwargs["config"],
            scripts=kwargs["scripts"],
            renderer=kwargs["renderer"],
        )
