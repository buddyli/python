<%inherit file="../system_base.tpl"/>

<%block name="content">
<div id="content"> <!-- Content begins here --> 
    <div class="box"> <!-- Box begins here -->
        <!--Standard form within a fieldset tag;-->
        <form method="post" action="/manage/super/add"><!-- Form -->
            <fieldset><legend>Administrator</legend>
                <%
                    user = data['member'] if data and 'member' in data else None
                %>

                <div class="input_field">
                    <label for="b">Account</label>
                    <input class="smallfield" name="account" type="text" value="${ user['account'] if 'account' in user else ''}" />
                </div>
                
                <div class="input_field">
                    <label for="b">Password</label>
                    <input class="smallfield" name="password" type="text" value="" />
                    <span class="field_desc"> Optional</span>
                </div>

                 <div class="input_field">
                    <label for="b">Level</label>
                    <input class="smallfield" name="level" type="text" value="${ user['level'] if 'level' in user else ''}" />
                </div>
                        
                <input class="submit" type="submit" value="Submit" />
            </fieldset>
        </form><!-- /Form -->
    </div> <!-- END Box-->
</div> <!-- END Content -->
</%block>