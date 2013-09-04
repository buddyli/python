<%inherit file="../system_base.tpl"/>

<%block name="content">
<div id="content"> <!-- Content begins here -->        
    <div class="box"> <!-- Box begins here -->
        <h2>Member List</h2>                           
        <!--Classical Table below, must be used with thead and tbody tags;-->
        <table cellspacing="0" cellpadding="0"><!-- Table -->
            <thead>
                <tr>
                    <th>Account</th>
                    <th>Level</th>
                    <th>Addtime</th>
                    <th>Action</th>
                </tr>
            </thead>
                
            <tbody>
                %if data and 'members' in data:
                    %for member in data['members']:
                    <tr class="${loop.cycle('alt', 'odd')}">
                        <td>${ member['account'] if 'account' in member else '--' }</td>
                        <td>${ member['level'] if 'level' in member else '--' }</td>
                        <td>${ member['addtime'] if 'addtime' in member else '--' }</td>
                        <td>
                        <a class="edit" href="/system/manager/edit?_id=${ member['_id'] }">edit</a>
                        <a class="delete" href="/system/manager/delete?_id=${ member['_id'] }${ '&_uniq=%s' % data['_uniq'] if '_uniq' in data else ''}" onclick="javascript:return confirm('Yes or No?')">delete</a>
                        </td>
                    </tr>
                    %endfor
                %endif
            </tbody>
        </table><!-- END Table -->
        <div class="box">
            <!-- Page Navigation -->
            %if 'pagenation' in data:
            <ul class="paginator">
                %for p in data['pagenation']:
                <li class="${ 'current' if p == data['cur_page'] else ''}"><a href="/system/manager/list?page=${ p }${ '&_uniq=%s' % data['_uniq'] if '_uniq' in data else ''}">${ p }</a></li>
                %endfor
            </ul>
            %endif
        <!-- /Page Navigation -->
        </div>
    </div> <!-- END Box-->
</div> <!-- END Content -->
</%block>