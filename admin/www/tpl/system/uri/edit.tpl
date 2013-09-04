<%inherit file="../system_base.tpl"/>

<%block name="content">
<div id="content"> <!-- Content begins here --> 
    <div class="box"> <!-- Box begins here -->
        <!--Standard form within a fieldset tag;-->
        <form method="post" action="/system/uri/add"><!-- Form -->
            <fieldset><legend>Administrator</legend>
                <%
                    item = data['item'] if data and 'item' in data else None
                %>

                <div class="input_field">
                    <label for="b">Account</label>
                    <input class="smallfield" name="name" type="text" value="${ item['name'] if 'name' in item else ''}" />
                </div>
                
                <div class="input_field">
                    <label for="b">Address</label>
                    <input class="bigfield" name="url" type="text" value="${ item['url'] if 'url' in item else ''}" />
                    <span class="field_desc"> 多个地址用半角逗号分割</span>
                </div>

                <input name="_id" type="hidden" value="${ item['_id'] if '_id' in item else ''}" />
                        
                <input class="submit" type="submit" value="Submit" />
            </fieldset>
        </form><!-- /Form -->
    </div> <!-- END Box-->
</div> <!-- END Content -->
</%block>