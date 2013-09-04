<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" dir="ltr">

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title><%block name="title">Website Name | Splash Manager</%block></title>

<%block name="global_css">
    <!-- Loading CSS file -->
    <style type="text/css" media="all">
    /* Load framework elements */
    @import url(${site_opt['static_url']}/static/m/css/framework.css);
    /* Now, lets set the style */
    @import url(${site_opt['static_url']}/static/m/styles/style_coffee.css);
    </style>
</%block>

    <style type="text/css">
        img { behavior: url(${site_opt['static_url']}/static/m/js/iepngfix.htc) !important; }
        .navbullet { behavior: url(${site_opt['static_url']}/static/m/js/iepngfix.htc) !important; }
    </style> 

<%block name="global_js">
    <!-- Loading javascript -->
    <script src="${site_opt['static_url']}/static/m/js/jquery.js" type="text/javascript"></script>
    <script src="${site_opt['static_url']}/static/m/js/jquery-ui.js" type="text/javascript"></script>
    <script src="${site_opt['static_url']}/static/m/js/functions.js" type="text/javascript"></script>
</%block>

</head>
<body>

<div id="container"> <!-- Container begins here -->  
    <div id="sidebar"> <!-- Sidebar begins here -->

    <%block name="siderbar">
        <div class="header logo"> <!-- Logo begins here -->
            <a href="javascript:;" title=""><img src="${site_opt['static_url']}/static/m/images/logo.png" alt="" /></a>
        </div> <!-- END Logo -->
                
        <div id="navigation"> <!-- Navigation begins here -->
            <div class="sidenav"><!-- Sidenav -->
                <%include file="inc/sidenav.tpl" />
            </div><!-- /Sidenav -->
        </div> <!-- END Navigation -->
        <div id="copyrights">
            <p><a href="javascript:;" title="">Splash Manager Theme<br />designed by Mastergreed</a>. Live Preview hosted on 
            <a href="javascript:;">WHB</a>.</p>
        </div>
    </%block>

    </div> <!-- END Sidebar -->
    <div id="primary"> <!-- Primary begins here -->
        <%include file="inc/top_nav.tpl" />

<%block name="content">        
    <div id="content"> <!-- Content begins here -->        
        <div class="box"> <!-- Box begins here -->
            <pre>
                Defualt content html.
            </pre>
        </div>
    <div>
</%block>

    </div> <!-- END Primary --> 
    <div class="clear"></div>
</div> <!-- END Container -->
</body>
</html>