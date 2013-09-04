<%inherit file="../system_base.tpl"/>

<%block name="content">
<div id="content"> <!-- Content begins here -->        
    <div class="box"> <!-- Box begins here -->
        <h2>Member List</h2>                           
        <!--Classical Table below, must be used with thead and tbody tags;-->
        <table cellspacing="0" cellpadding="0"><!-- Table -->
            <thead>
                <tr>
                    <th>地址</th>
                    <th>状态</th>
                </tr>
            </thead>
                
            <tbody>
                %if data and 'items' in data:
                    %for item in data['items']:
                    <tr class="${loop.cycle('alt', 'odd')}">
                        <td>${ item['url'] if 'url' in item else '--' }</td>
                        <td>${ '%s ...' % item['response'][0:100] if 'response' in item else '--' }</td>
                    </tr>
                    %endfor
                %endif
            </tbody>
        </table><!-- END Table -->
    </div> <!-- END Box-->
</div> <!-- END Content -->
</%block>