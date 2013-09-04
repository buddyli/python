<%inherit file="../system_base.tpl"/>

<%block name="content">
<div id="content"> <!-- Content begins here -->        
    <div class="box"> <!-- Box begins here -->
        <h2>Member List</h2>                           
        <!--Classical Table below, must be used with thead and tbody tags;-->
        <table cellspacing="0" cellpadding="0"><!-- Table -->
            <thead>
                <tr>
                    <th>名称</th>
                    <th>地址</th>
                    <th>Addtime</th>
                    <th>Action</th>
                </tr>
            </thead>
                
            <tbody>
                %if data and 'items' in data:
                    %for item in data['items']:
                    <tr class="${loop.cycle('alt', 'odd')}">
                        <td>${ item['name'] if 'name' in item else '--' }</td>
                        <td>${ '%s ...' % item['url'][0:40] if 'url' in item else '--' }</td>
                        <td>${ item['addtime'] if 'addtime' in item else '--' }</td>
                        <td>
                        <a class="edit" href="/system/uri/edit?_id=${ item['_id'] }">编辑</a>

                        <a class="edit" href="/system/uri/refresh?_id=${ item['_id'] }${ '&_page=%s' % data['_page'] if '_page' in data else ''}" onclick="javascript:return confirm('Yes or No?')">加载</a>

                        <a class="delete" href="/system/uri/delete?_id=${ item['_id'] }${ '&_page=%s' % data['_page'] if '_page' in data else ''}" onclick="javascript:return confirm('确定要删除[[${item['name']}]]\n\nYes or No?')">删除</a></td>
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