<%inherit file="../system_base.tpl"/>

<%block name="content">
<div id="content"> <!-- Content begins here --> 
    <div class="box"> <!-- Box begins here -->
        <!--Standard form within a fieldset tag;-->
        <form method="post" action="/system/manager/add"><!-- Form -->
            <fieldset><legend>Administrator</legend>
                <%
                    item = data['item'] if data and 'item' in data else None
                %>

                <div class="input_field">
                    <label for="b">Account</label>
                    <input class="smallfield" name="account" type="text" value="${ item['account'] if 'account' in item else ''}" />
                </div>
                
                <div class="input_field">
                    <label for="b">Password</label>
                    <input class="smallfield" name="password" type="text" value="" />
                    <span class="field_desc"> Optional</span>
                </div>

                 <div class="input_field">
                    <label for="b">Level</label>
                    <input class="smallfield" name="level" type="text" value="${ item['level'] if 'level' in item else ''}" />
                </div>

                <input name="_id" type="hidden" value="${ item['_id'] if '_id' in item else ''}" />
                        
                <input class="submit" type="submit" value="Submit" />
            </fieldset>
        </form><!-- /Form -->
    </div> <!-- END Box-->
</div> <!-- END Content -->
</%block>