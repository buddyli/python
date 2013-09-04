<%inherit file="../system_base.tpl"/>

<%block name="content">
<div id="content"> <!-- Content begins here --> 
    <div class="box"> <!-- Box begins here -->
        <!--Standard form within a fieldset tag;-->
        <form method="post" action="/manage/member/add"><!-- Form -->
            <fieldset><legend>member</legend>

                <div class="input_field">
                    <label for="a">Passport ID</label>
                    <input class="mediumfield" name="passport" type="text" value="" />
                    <span class="field_desc"> * Required</span>
                </div>

                <div class="input_field">
                    <label for="b">Password</label>
                    <input class="smallfield" name="password" type="text" value="" />
                    <span class="field_desc"> Optional</span>
                </div>

                <div class="input_field">
                    <label for="b">Username</label>
                    <input class="smallfield" name="username" type="text" value="" />
                </div>

                <div class="input_field">
                    <label for="b">Country</label>
                    <input class="smallfield" name="country" type="text" value="" />
                </div>

                <div class="input_field">
                    <label for="b">Shares</label>
                    <input class="smallfield" name="shares" type="text" value="" />
                </div>
                        
                <div class="input_field">
                    <label for="b">Mobile</label>
                    <input class="smallfield" name="mobile" type="text" value="" />
                </div>

                <div class="input_field">
                    <label for="b">Email</label>
                    <input class="smallfield" name="email" type="text" value="" />
                </div>

                <div class="input_field">
                    <label for="b">Address</label>
                    <input class="bigfield" name="address" type="text" value="" />
                </div>
                        
                <input class="submit" type="submit" value="Submit" />
            </fieldset>
        </form><!-- /Form -->
    </div> <!-- END Box-->
</div> <!-- END Content -->
</%block>