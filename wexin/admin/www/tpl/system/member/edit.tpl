<%inherit file="../system_base.tpl"/>

<%block name="content">
<div id="content"> <!-- Content begins here --> 
    <div class="box"> <!-- Box begins here -->
        <!--Standard form within a fieldset tag;-->
        <form method="post" action="/manage/member/add"><!-- Form -->
            <fieldset><legend>member</legend>
                <%
                    user = data['member'] if data and 'member' in data else None
                %>

                <div class="input_field">
                    <label for="a">Passport ID</label>
                    <input class="mediumfield" name="passport" type="text" value="${ user['passport'] if 'passport' in user else ''}" />
                    <span class="field_desc"> * Required</span>
                </div>

                <div class="input_field">
                    <label for="b">Password</label>
                    <input class="smallfield" name="password" type="text" value="" />
                    <span class="field_desc"> Optional</span>
                </div>

                <div class="input_field">
                    <label for="b">Username</label>
                    <input class="smallfield" name="username" type="text" value="${ user['username'] if 'username' in user else ''}" />
                </div>

                 <div class="input_field">
                    <label for="b">Country</label>
                    <input class="smallfield" name="country" type="text" value="${ user['country'] if 'country' in user else ''}" />
                </div>

                <div class="input_field">
                    <label for="b">Shares</label>
                    <input class="smallfield" name="shares" type="text" value="${ user['shares'] if 'shares' in user else ''}" />
                </div>
                        
                <div class="input_field">
                    <label for="b">Mobile</label>
                    <input class="smallfield" name="mobile" type="text" value="${ user['mobile'] if 'mobile' in user else ''}" />
                </div>

                <div class="input_field">
                    <label for="b">Email</label>
                    <input class="smallfield" name="email" type="text" value="${ user['email'] if 'email' in user else ''}" />
                </div>

                <div class="input_field">
                    <label for="b">Address</label>
                    <input class="bigfield" name="address" type="text" value="${ user['address'] if 'address' in user else ''}" />
                </div>
                        
                <input class="submit" type="submit" value="Submit" />
            </fieldset>
        </form><!-- /Form -->
    </div> <!-- END Box-->
</div> <!-- END Content -->
</%block>